#!/usr/bin/env python3
import csv
from os.path import basename
from datetime import date
import glob
import pandas as pd

directory = "/home/thomas-le/Desktop/xxxn/qsecofr"
newDir = "{0}/new".format(directory)
oldDir = "{0}/old".format(directory)
monthlyFile = "{0}/Qsecofr_Audit_Review_{1}.xlsx".format(directory, date.today().strftime("%b_%Y"))
servers = ["CAM","CATS","CLUX","DFSNZ1","FRANCE","GDC","GVA","HKGA","HNL","INDO","ITL","KOREA","LAX1","MIDEAST","MIDPAC","PAD1","PAX1","PRC","SAP2PFS", "SFO2", "SFO", "SIN2", "SYD"]

def checkFiles():
  missedFiles = []

  for server in servers:
    if glob.glob("{0}/*{1}*".format(newDir,server)) == []:
      missedFiles.append(server)

  if missedFiles == []:
    return True
  else:
    print("Below file(s) are missed. Please check w/ L2.")
    for file in missedFiles:
      print(file)
    return False

def createReport():
  newFiles = sorted(glob.glob("./{0}/*.csv".format(newDir)))
  oldFiles = sorted(glob.glob("./{0}/*.csv".format(oldDir)))
  for newFile, oldFile in zip(newFiles, oldFiles):
    old = pd.read_csv(oldFile,encoding='unicode_escape',header=None).iloc[:,3:]
    new = pd.read_csv(newFile,encoding='unicode_escape',header=None).iloc[:,3:]
    result = pd.concat([new,old]).drop_duplicates(keep=False)
    if not result.empty:
      results = pd.concat([results,result])

def createExcel():
  with pd.ExcelWriter(monthlyFile) as writer:
    for csvf in sorted(glob.glob("{0}/*".format(newDir))):
      sheetname = basename(csvf).split('_')[0]
      reader = pd.read_csv(csvf,encoding="unicode_escape",header = None)
      reader.to_excel(writer,index=False,header=False,sheet_name=sheetname)

if checkFiles():
  createReport()
  createExcel()
