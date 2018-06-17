#!/bin/bash

# Updates the system
sudo apt-get update


# Install all necessary dependencies
sudo apt-get -y install libpcre3 libpcre3-dbg libpcre3-dev \
build-essential autoconf automake libtool libpcap-dev libnet1-dev \
libyaml-0-2 libyaml-dev zlib1g zlib1g-dev libmagic-dev libcap-ng-dev \
libjansson-dev pkg-config libnetfilter-queue-dev checkinstall


# Run scripts in chain
# ./Shell/installSuricata.sh
