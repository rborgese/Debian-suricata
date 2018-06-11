#!/bin/bash
wlan=$(ls /sys/class/net | grep ^wlp)
sudo /usr/bin/suricata -c /etc/suricata/suricata.yaml -i $wlan
