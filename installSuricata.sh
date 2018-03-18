wget http://www.openinfosecfoundation.org/download/suricata-3.1.tar.gz
tar -xvzf suricata-3.1.tar.gz
cd suricata-3.1

./configure --enable-nfqueue --prefix=/usr --sysconfdir=/etc --localstatedir=/var
make
sudo make install-full

rm -r suricata-3.1.tar.gz
rm -r suricata-3.1

sudo /usr/bin/suricata -x /etc/suricata//suricata.yaml -i wlan0
