#!/usr/bin/env bash
wget http://www.openinfosecfoundation.org/download/suricata-4.0.4.tar.gz

tar -xvzf suricata-4.0.4.tar.gz
cd suricata-4.0.4

./configure --enable-nfqueue --prefix=/usr --sysconfdir=/etc --localstatedir=/var
make
sudo checkinstall

cd ..

sudo rm -r suricata-4.0.4.tar.gz
