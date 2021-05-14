#!/usr/bin/env python3

import sqlite3
import sys

email = sys.argv[1]

conn = sqlite3.connect('D:/2021/1-Code/LBN/3-Automate password/sqlite/lbn_as400pw.db')
cur = conn.cursor()
cur.execute("SELECT * FROM USERS WHERE email LIKE :email",{"email": email})
row = cur.fetchone()
if isinstance(row,tuple):
    cur.execute("SELECT server_id FROM SERVERS WHERE server_id IN \
                 (SELECT server_id FROM USERS_SERVERS \
                  WHERE user_id = (SELECT user_id FROM USERS WHERE email LIKE :email))",{"email": email})
    servers = cur.fetchall() 
    print(servers)    
    for server in servers:
        print(server)
else:
    print("YOUR EMAIL IS NOT FOUND!")
conn.close()
