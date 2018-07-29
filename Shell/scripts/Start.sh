#!/bin/bash

currentuser=$(whoami)
currentdir="$PWD/Shell/scripts"


# Required scripts

chmod u+x Shell/scripts/startSuricata.sh
chmod u+x Shell/scripts/rm_checkSuricata.sh
chmod u+x Shell/scripts/tail_suricata.sh

# Require sudo access
writedeps="$currentuser ALL=(ALL) NOPASSWD: $currentdir/deps_suricata.sh"
echo $writedeps | sudo tee --append /etc/sudoers.d/debianSuricata
sudo chown root:root Shell/scripts/deps_suricata.sh
sudo chmod 700 Shell/scripts/deps_suricata.sh

writeinstall="$currentuser ALL=(ALL) NOPASSWD: $currentdir/installSuricata.sh"
echo $writeinstall | sudo tee --append /etc/sudoers.d/debianSuricata
sudo chown root:root Shell/scripts/installSuricata.sh
sudo chmod 700 Shell/scripts/installSuricata.sh

writerm="$currentuser ALL=(ALL) NOPASSWD: $currentdir/rm_makeSuricata.sh"
echo $writerm | sudo tee --append /etc/sudoers.d/debianSuricata
sudo chown root:root Shell/scripts/rm_makeSuricata.sh
sudo chmod 700 Shell/scripts/rm_makeSuricata.sh
chmod u+x Shell/scripts/rm_makeSuricata.sh



# Tests
chmod u+x Shell/tests/bad_cd.sh
chmod u+x Shell/tests/cd.sh
chmod u+x Shell/tests/ls.sh
chmod u+x Shell/tests/sudoTest.sh

# For development only ---> ignores future changes in Outputs/
# git update-index --assume-unchanged Outputs/*

# Run scripts in chain
# ./Shell/deps_suricata.sh
