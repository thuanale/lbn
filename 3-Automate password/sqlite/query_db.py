#!/usr/bin/env python3

import sqlite3
import sys

email = 'V.dang@linkbynet.com'#sys.argv[1]

conn = sqlite3.connect('D:/2021/1-Code/LBN/3-Automate password/sqlite/lbn_as400pw.db')
cur = conn.cursor()
cur.execute("SELECT * FROM USERS WHERE email LIKE :email",{"email": email})
row = cur.fetchone()
if isinstance(row,tuple):
    print(row)
else:
    print("YOUR EMAIL IS NOT FOUND!")
conn.close()
