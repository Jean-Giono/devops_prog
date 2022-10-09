#!/bin/bash

#------------------
#Author:Jean-Giono
#------------------

#dézippage et désarchivage dans /home/travail

file_to_decompress="/archives/"$(ls -t /archives | grep archive_travail | head -n1)

tar -xzf $file_to_decompress -C /
