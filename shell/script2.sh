#!/bin/bash

#--------------------
#Author: Jean-Giono
#Date: 04/08/2022
#--------------------


cur_date=$(date '+%d/%m/%Y')
URL=$1 #argument argv[1], should be a url valid or not
response=$(curl -s -w "%{http_code}" "$URL" --output /dev/null --silent)


echo "$cur_date $URL $response" | tee -a ficlog.txt

