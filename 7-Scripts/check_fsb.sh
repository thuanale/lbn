#!/usr/bin/env bash
USER=${1:-OPSTHUAN}
SERVER=${2^^}

check_dstq(){
  SFO="$1"
  while IFS="" read -r LINE
  do
	  read SERVER PTY <<< $LINE
    echo ssh ${USER}@${SERVER}.dfs "system 'HLDDSTQ DSTQ('${SFO}') PTY(*'${PTY}')';system 'RLSDSTQ DSTQ('${SFO}') PTY(*'${PTY}')'"
    done < <(
      for SERVER in  CAM CATS CLUX GDC GVA HKGA HNL INDO ITL KOREA LAX1 MIDEAST MIDPAC PRC SFO SFO2 SIN2 SYD SAP2PFS
      do 
		    ssh ${USER}@${SERVER}.dfs "system 'WRKDSTQ QUEUE('${SFO}')'" | awk '/'${SFO}'.*Rty-Fail/{printf("%-8s%-8s\n","'${SERVER}'",$2);}'
      done
  )
  for SERVER in  CAM CATS CLUX GDC GVA HKGA HNL INDO ITL KOREA LAX1 MIDEAST MIDPAC PRC SFO SFO2 SIN2 SYD SAP2PFS
  do 
    ssh ${USER}@${SERVER}.dfs "system 'WRKDSTQ QUEUE('${SFO}')'" | grep -A2 'Queue Name' | grep -v Queue | awk '{printf("%s/'${SFO}' (%s): %s\n", "'${SERVER}'", $2, $9);}'
  done
}

wrkactjob(){
  for sbs in "$@"
  do
    cmd+="$sbs "
  done
  ssh ${USER}@${SERVER}.DFS "system 'wrkactjob sbs(${cmd})'" | grep -E '[0-9]{6}.*'
}

wrkoutq(){
  file=$(mktemp)
  ssh ${USER}@${SERVER}.DFS "system 'wrkoutq outq(QEZJOBLOG)'" > $file
  for job in "$@"
  do
    echo "${job} :"
    grep "${job}" "$file" | tail -1
  done
  rm -f "${file}"
}

case ${3} in
precheck)
  #ssh ${USER}@${SERVER}.DFS "system 'WRKMLBSTS'" #no permission to run from UNIX
  echo "TAPE DRIVES STATUS:"
  ssh ${USER}@${SERVER}.DFS "system 'DSPTAPSTS'" | awk '/TAP[0-9]{,3}/'
  echo "DSTQ STATUS:"
  ssh ${USER}@${SERVER}.DFS "system 'WRKDSTQ'" | grep -E '(Normal|High).*[AZaz].*'
  echo -n "Available tapes: "
  
  case "${SERVER}" in
  DRSAP2PF) 
    ssh ${USER}@${SERVER}.DFS "system 'WRKMEDBRM TYPE(*EXP) LOC(TAPMLB09) MEDCLS(ULTRIUM5) SYSNAME(*LCL)'" | awk '/50[0-9]{4}/{print($1)}' | wc -l
    ;;

  *)
    ssh ${USER}@${SERVER}.DFS "system 'WRKMEDBRM TYPE(*EXP) LOC(LTO5DRT) MEDCLS(ULTRIUM5) SYSNAME(*LCL)'" | awk '/55[0-9]{4}/{print($1)}' | wc -l
    ;;
  esac
  echo -n "Today is: "
  ssh ${USER}@${SERVER}.DFS "system 'DSPSYSVAL SYSVAL(QDATETIME)'" | awk '/'${SERVER}'/{print($5,$6)}'
  echo "CHECKING JOBS:"
  case ${SERVER} in
  CLUX|FRANCE|GDC|HKGA)
	  wrkactjob QBATCH DMSSBS POSBS PVPSBS PISBS
	  ;;

  CATS)
    wrkactjob QBATCH CATSBS CATSBSSIN CATSBSTPE CATSBSIND
	  ;;

  GVA)
  	wrkactjob QBATCH QPGMR SCOMSYS POSBS PVPSBS DMSSBS
	  ;;

  HNL)
	  wrkactjob QBATCH DMSSBS POSBS PVPSBS PISBS
  	wrkoutq SAPINVP_11
	  ;;

  LAX1)
	  wrkactjob QBATCH DMSSBS POSBS PVPSBS PISBS
  	wrkoutq DMSPLU041
	  ;;

  MIDEAST)
	  wrkoutq LVNSALEFTP SAPINVP_31 DFACT001 SKU533C
  	wrkactjob QBATCH PISBS
	  ;;

  MIDPAC)
	  wrkactjob QBATCH BATCH1 DMSSBS PLANNING POSBS PVPSBS PISBS
  	wrkoutq SAPINVP_58
	  ;;

  PRC)
	  wrkactjob QBATCH DMSSBS POSBS PVPSBS PISBS
  	wrkoutq SAPINVP_91
	  ;;

  SFO)
	  wrkactjob QBATCH MPRSBS DMSSBS POSBS PVPSBS GDCSBS QCTL
  	wrkoutq DMSLV_JOB
	  ;;

  SFO2)
	  wrkactjob QBATCH MPRSBS PVPSBS DMSSBS POSBS
  	wroutq GDD_JOB_S STRDLYJOB NIGHTJOB DFACT001 ID_RSTCONS				
	  ;;

  SIN2)
	  wrkactjob QBATCH QPGMR PLANNING OPERATIONS IPSQSBS MTHEND POSBS PVPSBS DMSSBS PISBS
	  ;;

  SYD)
	  wrkactjob QBATCH QPGMR NIGHTSHIFT QBATCHFAST POSBS PVPSBS DMSSBS PISBS
	  wrkoutq SAPINVP_73 SAPINVP_75
	  ssh ${USER}@SIN2.DFS "system 'wrkoutq outq(qezjoblog)'" | grep MPR_SO_GEN | tail -1
	  ;;

   *) wrkactjob "QBATCH";;
   esac
   ;;

postcheck)
  reg='^SFO[2]?'
  ssh ${USER}@${SERVER}.DFS "system 'WRKDSTQ'" | grep -E '(Normal|High).*[AZaz].*'
  ssh ${USER}@${SERVER}.DFS "system 'WRKMQM';system 'WRKACTJOB SBS(QSYSWRK RBTSLEEPER MAXAVASBS)'"
  [[ "$SERVER" =~ $reg ]] && check_dstq ${SERVER}
  ;;
*)
   echo "INVALID CASE."
   ;;
esac
