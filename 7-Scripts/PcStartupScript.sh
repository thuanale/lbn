#!/usr/bin/bash

AgentPid="$HOME/AGENT.PID"

if (( $(grep -c ssh-agent <(ps aux)) >= 2 )) && [[ -s $AgentPid ]]; then
  echo "+++ LOAD ENVIRONMENT PARAMETER+++"
  source $AgentPid
else
  echo "+++ START SSH-AGENT +++"
  eval $(ssh-agent -s)
  env | grep -i ssh > $AgentPid
fi
echo "+++ LOAD KEY FOR GIT +++"
ssh-add $HOME/.ssh/id_ed25519
echo "+++ LOAD KEY FOR DFS BASTION HOSTS +++"
ssh-add $HOME/.ssh/ssh-pri
echo "+++ Local port forwarding for AS400 Monitoring webapp. +++"
ssh -L 8989:10.242.0.38:3389 t.le@172.21.198.39 -N -f
echo "+++ Dynamic port forwarding for other Application at DFS. +++"
ssh -C -D 8888 t.le@172.21.198.39 -N -f
echo "END."

