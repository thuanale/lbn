#!/usr/bin/env python3
import csv
from openpyxl import Workbook
from os.path import basename,splitext
import glob
import zipfile
from io import TextIOWrapper

directory = "/home/thomas-le/Desktop/xxxn"
for QsecorfFile in glob.glob("{0}/AS400_ATSECOFR_*.zip".format(directory)):
  wb = Workbook(write_only = True)
  with zipfile.ZipFile(QsecorfFile) as zf:
    for csvfile in zf.namelist():
      with zf.open(csvfile) as csvf:
        ws = wb.create_sheet(title = csvfile.split('_')[0])
        reader = csv.reader(TextIOWrapper(csvf,encoding='utf-8',newline=''))
        for row in reader:
          ws.append(row)
  wb.save(filename="{0}.xlsx".format(splitext(basename(QsecorfFile))[0]))

