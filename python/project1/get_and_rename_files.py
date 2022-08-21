#Jean-Giono
#10/08/2022

# installez wget si ce n'est fait, auquel cas l'import ne fonctionnera pas
# la commande est la suivante, depuis un terminal : pip install wget
import wget
import os
import glob
from zipfile import ZipFile

def renameFile(url, dest_name):
    '''
        url : l'adresse de votre fichier zippé
        dest_name : le nom du dossier dans lequel seront dézippés vos fichiers
        
        ex : url = "https://github.com/Jean-Giono/devops_prog/blob/main/python/project1/flags.zip"
             dest_name = "flagBis"
    '''

    rep_filerr = ""
    # création d'un dossier portant le nom indiqué
    try:
        os.mkdir(dest_name)
        print("[+] Le dossier %s a bien été créé!\n" % dest_name)
    except FileExistsError:
        print("Ce nom de dossier existe déja!\nSouhaitez-vous changer de nom de dossier ?(o/n)\n")

        while(rep_filerr != "o" and rep_filerr != "n"):
            rep_filerr = str(input()).lower()
            if rep_filerr == "n":
                print("\nLe contenu du fichier téléchargé sera donc dézippé dans l'actuel dossier nommé %s!\nA vos risques et périls!\n" % dest_name)
            elif rep_filerr == "o":
                print("\nVeuillez donc essayer de nouveau!\n")
                exit()
            else:
                print("\nJe ne vous ai pas compris ...\nVeuillez saisir une réponse valable, dans la liste suivante : o, n, O, N!\n")
    
    # suppression de tous les fichiers zip apparentés à flags.zip
    path_flag = "flags*.zip"
    for file in glob.glob(path_flag):
        os.remove(file)
    
    # téléchargement du fichier zippé à l'adresse indiquée
    flags = wget.download(url, bar=None)
    print("[+] Le fichier %s est bien téléchargé!\n" % flags)


    print("[+] Renommage des fichiers : \n")
    
    # dézippage des fichiers sauf celui nommé missing.png
    with ZipFile(flags, 'r') as flg:
        lisfOfFileNames = flg.namelist()
        for fileName in lisfOfFileNames:
            if not fileName.startswith('missing'):
                flg.extract(fileName, dest_name)
                file_decomp = os.path.splitext(fileName)
                new_filename = file_decomp[0].upper()[:2] + file_decomp[1]
                # renommage des fichiers dans le répertoire
                os.rename(dest_name+"/"+fileName, dest_name+"/"+new_filename)
                print("\t[+] le fichier nommé %s devient => %s" % (fileName, new_filename))
            else:
                continue
    
    print("\n[+] Tous vous fichiers ont bien été extraits dans le dossier %s!\n" % dest_name)


url = "https://github.com/Jean-Giono/devops_prog/blob/main/python/project1/flags.zip"
dest_name = "flagBis"

renameFile(url, dest_name)
