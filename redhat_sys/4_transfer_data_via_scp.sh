#!/bin/bash


# récupération de l'archive la plus récente dans /archives/
file_to_copy="/archives/"$(ls -t /archives | grep archive_travail | head -n1)

#echo $file_to_copy

# copie via scp de ce fichier dans le home directory de l'utilisateur jeangiono1 (c'est une autre machine)
scp -i /home/jeangiono/.ssh/id_rsa_jg1 $file_to_copy jeangiono1@192.168.0.11:~/
