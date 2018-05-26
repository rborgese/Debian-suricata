wget http://www.openinfosecfoundation.org/download/suricata-4.0.4.tar.gz
tar -xvzf suricata-3.1.tar.gz
cd suricata-3.1

./configure --enable-nfqueue --prefix=/usr --sysconfdir=/etc --localstatedir=/var
make
sudo checkinstall

rm -r suricata-3.1.tar.gz
rm -r suricata-3.1
