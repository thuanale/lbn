#!/usr/bin/env python3
###########################################################################################
# Description: Send email with attachment                                                 #
# Author:                                                                                 #
# Version:                                                                                #
# Last update:                                                                            #
# Usage:                                                                                  #
# python -s "<Subject>" -f "<from>" -t "<receiver1>,...,<receivern>" -a "<file1>,<file2>" #
###########################################################################################
from email.message import EmailMessage
from smtplib import SMTP
from os.path import *

MsgBody = """
  <html>
    <head></head>
    <body>
      <p>Hi Team,</p>
      <p>This is only a test email with hyper link & attached file. 
        <a href="http://www.yummly.com/recipe/Roasted-Asparagus-Epicurious-203718">
        recipie
        </a>
      </p>
      <p>Best regards</p>
      <p>-----------</p>
      <p>This is auto email, please don't reply</p>
    </body>
  </html>
"""
attachedFile = 'TAPE.TXT'
# Declare email
msg = EmailMessage()

# Set header of email
msg.add_header("Subject","Hello world")
msg.add_header('From',"noreply@dfs.com")
msg.add_header('To',"thuanale@gmail.com,thuanlevt19@gmail.com")
msg.add_header("Content-Type","multipart/mixed")

# Body of email
msg.add_attachment(MsgBody,subtype="html",disposition="inline")
with open('TAPE.TXT','rb') as fp:
  msg.add_attachment(fp.read(),maintype="application",subtype="txt",disposition="attachment",filename="TAPE")


with SMTP('smtprelaysg.dfs.com:25') as mbx:
    mbx.send_message(msg)

