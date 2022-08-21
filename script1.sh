#!/bin/bash

<<INFOS
#Author: Jean-Giono
#Date: 04/08/2022
INFOS

#number=64
number=$((RANDOM % 10)) #nb aléatoire entre 1 et 10
found=0
cpt=0

echo "Bienvenue dans ce jeu!"
echo -e "Il consiste à trouver un nombre caché, en un minimum d'essais!\nA vous!"

while [[ $found == 0 ]]
do
  read -p "Saisissez un nombre ? " nb
 
  ((cpt++))
  if [[ ${nb} -gt $number ]]
  then
     echo "c'est moins!"
  fi

  if [[ ${nb} -lt $number ]]
  then
    echo "c'est plus!"
  fi

  if [[ ${nb} -eq $number ]]
  then
    found=1
    echo "bravo!"
    echo "vous l'avez trouvé en ${cpt} coup(s)!"
  fi
done

