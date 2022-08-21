import os
import argparse
from cryptography.fernet import Fernet

class Crypt:
    def __init__(self):
        self.key = b'kC0WStnLL0vfKaDzgdVpc0FGT-wbtsA8gkKYNe4WaL8='
        self.fernet = Fernet(self.key)

    def encrypt(self, file_path):
        base_name = os.path.basename(file_path).split('.')[0]
        out_file = base_name + ".enc"

        if os.path.exists(out_file):
            print("ce fichier existe déjà\n")
            exit()
        else:
            with open(file_path, 'rb') as f:
                data = f.read()
            
        encrypted = self.fernet.encrypt(data)

        with open(out_file, 'wb') as f:
            f.write(encrypted)
        
        print("fichier encrypté :", out_file)


    def decrypt(self, file_path, out_ext="dec"):
        base_name = os.path.basename(file_path).split('.')[0]
        out_file = f"{base_name}.{out_ext}"

        if os.path.exists(out_file):
            print("ce fichier existe déjà\n")
            exit()
        else:
            with open(file_path, 'rb') as f:
                data = f.read()
            
        #decrypted = str(self.fernet.decrypt(data),'utf-8')

        #with open(out_file, 'w') as f:
            #f.write(decrypted)
        
        decrypted = self.fernet.decrypt(data)

        with open(out_file, 'wb') as f:
            f.write(decrypted)

        print("fichier décrypté :", out_file)

# python3 crypt.py -e(encrypt) -d(decrypt) -f(file)

parser = argparse.ArgumentParser()

parser.add_argument('-e', '--encrypt', help="Encrypte le fichier")
parser.add_argument('-d', '--decrypt', help="Décrypte le fichier")

args = parser.parse_args()

crypt = Crypt()

if args.encrypt:
    crypt.encrypt(args.encrypt)
    print("fichier à encrypter :", args.encrypt)
elif args.decrypt:
    crypt.decrypt(args.decrypt)
    print("fichier à décrypter :", args.decrypt)