#!/usr/bin/env python3

import sqlite3
import sys

email = sys.argv[1]
as400_id = sys.argv[2]

conn = sqlite3.connect('./lbn_as400pw.db')
cur = conn.cursor()
cur.execute("SELECT * FROM USERS WHERE email LIKE :email AND as400_id LIKE :as400_id",{"email": email,"as400_id": as400_id})
row = cur.fetchone()
if isinstance(row,tuple):
    cur.execute("SELECT server_id, server_name FROM SERVERS WHERE server_id IN \
                 (SELECT server_id FROM USERS_SERVERS \
                  WHERE user_id = (SELECT user_id FROM USERS WHERE email LIKE :email AND as400_id LIKE :as400_id))",{"email": email,"as400_id": as400_id})
    servers = cur.fetchall() 
    print(servers)    
else:
    print("YOUR EMAIL IS NOT FOUND!")
conn.close()
