#!/bin/bash

# Download suricata 4.0.4
wget http://www.openinfosecfoundation.org/download/suricata-4.0.4.tar.gz

# Uncompress file and change directory to extracted folder
tar -xvzf suricata-4.0.4.tar.gz
cd suricata-4.0.4


# Configure Installation, make, and install with checkinstall for easy removal
./configure --enable-nfqueue --prefix=/usr --sysconfdir=/etc --localstatedir=/var
make
sudo checkinstall

# Change to parent directory
cd ..

# Remove downloaded file
sudo rm -r suricata-4.0.4.tar.gz

# For now Suricata-4.0.4 uncompressed folder stays but in the future might be removed
# sudo rm -r suricata-4.0.4
