#Jean-Giono
#12/08/2022

import argparse
import requests as req
import subprocess

URL = "http://149.202.54.27/devoteam"

parser = argparse.ArgumentParser("password generator for a user")

parser.add_argument('-u', '--user', help="user name")
parser.add_argument('-g', '--generate', help="pwd length to generate for the user", default='')

args = parser.parse_args()

u_name = args.user
u_pwd_len = args.generate

if u_pwd_len == '':
    pwd_gen = u_pwd_len
else:
    pwd_gen = subprocess.check_output(["python3", "gen_passwd.py", "-l", u_pwd_len]
                ).decode('utf-8')

    if u_pwd_len.isnumeric():
        if len(pwd_gen) > int(u_pwd_len)+1:
            print(pwd_gen)
            exit()
    else:
        print(pwd_gen)
        exit()

print("[+] Hello %s! Votre mot de passe est: %s" % (u_name, pwd_gen))
#print(type(u_name))

payload = {'username': u_name, 'password': pwd_gen}
req_text = req.post(url=URL, json=payload).text

print(req_text) #{todo bem}
