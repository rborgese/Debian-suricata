#!/bin/bash

# Required scripts
chmod u+x Shell/scripts/deps_suricata.sh
chmod u+x Shell/scripts/installSuricata.sh
chmod u+x Shell/scripts/startSuricata.sh
chmod u+x Shell/scripts/rm_makeSuricata.sh
chmod u+x Shell/scripts/rm_checkSuricata.sh
chmod u+x Shell/scripts/tail_suricata.sh

# Tests
chmod u+x Shell/tests/bad_cd.sh
chmod u+x Shell/tests/cd.sh
chmod u+x Shell/tests/ls.sh
chmod u+x Shell/tests/sudoTest.sh

# For development only ---> ignores future changes in Outputs/
# git update-index --assume-unchanged Outputs/*

# Run scripts in chain
# ./Shell/deps_suricata.sh
