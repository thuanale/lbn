#!/bin/bash
###################################################
# Description: add or remove member from database #
# Author: thomas.le@accenture.com                 #
# Version: 1.0                                    #
# Last update: 24-Jun-2022                        #          
###################################################

dir=$(dirname $0)
db="$dir/lbn_as400pw.db"
cp "${db}" "${db}.bk_$(date +%y%m%d%H%M%S)"
printMsg () { cat << EOF
Enter number to choose option:
1. Insert new
2. Remove old
3. Show all users
9. Quit
EOF
}

# Get info
getInfo() {
  while true; do
  read -p "Enter candidate email: " -r email
  read -p "Enter candidate as400 id: " -r id
  read -p "Confirm (Y/n/q)?" -r confirm
  case ${confirm,,} in
    n) echo "Please enter info again";;
    q) echo "Exit" & exit;;
    *) 
      echo "Email is $email"
      echo "ID is $id"
      break
    ;;
    esac
  done
}

#Insert info of new member
insertNew () {
  getInfo
  sqlite3 $db 'insert into users (email,as400_id) values ("'${email}'","'${id}'")'
  userId=$(sqlite3 $db 'select user_id from users where email = "'${email}'" and as400_id = "'${id}'";')

# Except for DRs, we have 44 servers in total.
# CMD: select * from servers
  for i in {1..44};do 
    sqlite3 $db 'insert into users_servers values ("'$userId'","'${i}'")'
  done
}

# Remove info of ex-member
removeOld () {
  getInfo
  userId=$(sqlite3 $db 'select user_id from users where email = "'${email}'" and as400_id = "'${id}'";')
  sqlite3 $db 'delete from users where user_id = "'${userId}'";'
  sqlite3 $db 'delete from users_servers where user_id = "'${userId}'";'
}

# Show all members:
showAll() {
  sqlite3 $db 'select * from users;'
}

# Main program
while true; do
  printMsg
  read -p "Your option is: " -r option
  case $option in
  1) insertNew ;;
  2) removeOld ;;
  3) showAll ;;
  9) echo "EXIT" & exit;;
  esac
    
  read -p "Again (Y/n)?" -r again

  case ${again,,} in
  n) echo "Exit" & exit;;
  *) clear ;;
  esac
done

