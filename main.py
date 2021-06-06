import re
username=input("Enter the username")
password=input().split(",")
criteria=re.compile(r"^([a-z0-9A-Z$#@]{6,12})")
for pwd in password:
    if criteria.fullmatch(pwd):
        print(pwd)
