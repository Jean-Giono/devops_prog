#!/bin/bash

#-------------------------
#Author:Jean-Giono
#Date:26/08/2022
#-------------------------


REPARCHI=/home/travail

#mkdir /archives/

archive_name=$(date +'%Y%m%d_%H-%M-%S')'_archive_travail.tar.gz'
tar -zcf /archives/$archive_name $REPARCHI > /dev/null 2>&1

nb_elem=$(ls /archives | grep archive_travail | wc -l)

if [ $nb_elem -gt 5 ]
then
  rm /archives/$(ls -t /archives | grep archive_travail | tail -n1)
fi
