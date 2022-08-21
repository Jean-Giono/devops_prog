#!/bin/bash

#---------------------------
#Author:Jean-Giono
#Date:05/08/2022
#---------------------------

NBARG=1
MISSINGARGS=20
URLFILE=https://github.com/Jean-Giono/devops_prog/blob/main/tp3-files.zip

n_user=$1
this_user=$(whoami)

if [ $# -ne "$NBARG" ]
then
  # arrêt du script si aucun ou plus d'un argument(s) fourni(s)
  echo "[+] fin du script! aucun ou plusieurs argument(s) fourni(s) ..."
  echo "[+] veuillez fournir un et un seul argument au prochain lancement!"
  exit $MISSINGARGS
else
 #suppression de l'utilisateur, si existant
 if id -u "$n_user" >/dev/null 2>&1; then
  sudo killall -u $n_user
  # ici je gère des pb de droits
  # je supprime le home de l'utilisateur puisque le userdel ne le fait proprement même avec l'option -r
  # j'ai passé une heure avant de me rendre compte que le programme adduser était plus convivial que useradd ... 
  sudo chown $this_user /home/$n_user/.*
  rm -r /home/$n_user 
  sudo userdel $n_user
  echo "[+] $n_user existe déjà et a été supprimé!"
 fi
 #creation de l'utilisateur dont le nom est fourni en paramètre
 sudo useradd -m -d /home/$n_user $n_user
 echo "[+] $n_user a bien été (re)créé!"
 #suppression de l'archive si déjà existante
 rm -r /tmp/tp3-*
 #telechargement d'un dossier zippé
 wget -q -P /tmp $URLFILE
 #l'utilisateur courant, devient le propriétaire du home directory du nouvel utilisateur
 sudo chown $this_user /home/$n_user
 #dezippage du fichier téléchargé
 zippedfile=$(ls -l /tmp | grep tp3 | tail -c 14)
 unzip -q /tmp/$zippedfile -d /home/$n_user/
 #remplacement de la chaîne "User" par le nom du nouvel utilisateur dans "user.html"
 filefullpath=$(find /home/$n_user/ -name user.html)
 #echo $filefullpath
 sed -i "s/User/$n_user/" $filefullpath
 sudo cp -p $filefullpath /var/www/html/ #preserve mode for permissions
fi

echo -e "Toutes les opérations ont été effectuées avec succès! \nSouhaitez-vous afficher votre magnifique page web ? (o/n)"
read rep

case $rep in
  [nN]) 
    ;;
  [oO])
    # démarrage du serveur web
    sudo service apache2 restart
    xdg-open http://localhost/user.html
    # arrêt du serveur web
    sudo service apache2 stop
    ;;
esac

echo "Au revoir $n_user! :-)"

exit 0
