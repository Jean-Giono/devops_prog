sudo groupadd rh
sudo groupadd compta
sudo groupadd responsable
sudo groupadd directeur
sudo groupadd secretariat

sudo useradd -G rh,users -p $(openssl passwd -l "caroline") caroline
sudo useradd -G rh,users -p $(openssl passwd -l "geraldine") geraldine
sudo useradd -G compta,users -p $(openssl passwd -l "jeanlouis") jeanlouis
sudo useradd -G compta,users -p $(openssl passwd -l "gertrude") gertrude
sudo useradd -G compta,responsable,users -p $(openssl passwd -l "bernard") bernard
sudo useradd -G secretariat,users -p $(openssl passwd -l "kevin") kevin
sudo useradd -G secreatariat,directeur,users -p $(openssl passwd -l "ryan") ryan

sudo usermod -aG users $USER

sudo mkdir -p /home/travail/{rh,compta/responsable,secreatariat/pdg,commun,secret/confidentiel}

sudo chmod 070 -R /home/travail/
sudo chmod 010 /home/travail/secret
sudo chmod 050 /home/travail/

sudo chgrp -R users /home/travail
sudo chgrp rh /home/travail/rh
sudo chgrp secreatariat /home/travail/secreatariat
sudo chgrp compta /home/travail/compta
sudo chgrp responsable /home/travail/compta/responsable
sudo chgrp directeur /home/travail/secreatariat/pdg
