#Jean-Giono
#12/08/2022
#tp5 - exo1 - Variante b

import argparse
import requests as req
from bs4 import BeautifulSoup

URL = "https://www.random.org/passwords/"

parser = argparse.ArgumentParser("password generator")

parser.add_argument('-l', '--length', help="pwd length")
parser.add_argument('-n', '--number', help="number of pwd to generate", default='1')

args = parser.parse_args()

pwd_len = args.length
pwd_nb = args.number

try:
    int_pwd_len = int(pwd_len)
except ValueError:
    print("[-] La longueur du mot de passe renseigné est : %s\n" % pwd_len)
    print("\tLa longueur doit être un chiffre ou un nombre! Veuillez réessayer!\n")
    exit()

if not(int_pwd_len >= 6 and int_pwd_len <= 16):
    print("[-] La longueur du mot de passe renseigné est : %d\n" % int_pwd_len)
    print("\tLa longueur du mot de passe doit être comprise entre 6 et 16! Veuillez réessayer!\n")
    exit()

try:
    int_pwd_nb = int(pwd_nb)
except ValueError:
    print("[-] Le nombre renseigné, de mots de passe à générer est : %s\n" % pwd_nb)
    print("\tLe nombre de mots de passe à générer, doit être un chiffre ou un nombre! Veuillez réessayer!\n")
    exit()

if not(int_pwd_nb >= 1 and int_pwd_nb <=50):
    print("[-] Le nombre renseigné, de mots de passe à générer est : %d\n" % int_pwd_nb)
    print("\tLe nombre de mots de passe à générer, doit être compris entre 1 et 50! Veuillez réessayer!\n")
    exit()

payload = {'num': pwd_nb, 'len': pwd_len, 'format': 'html', 'rnd': 'new'}
req_text = req.get(URL, payload).text

bs = BeautifulSoup(req_text, 'html.parser')
all_pwd = bs.find("ul", attrs={'class': 'data'}).find_all("li")

pwds = []
for pwd_ in all_pwd:
    pwds.append(pwd_.text)

#print("[+] Vous avez demandé à générer %d mot(s) de passe, de %d caractères chacun! Ci-après les mots de passe générés:" % (int_pwd_nb, int_pwd_len))
print(""+', '.join(pwds))
