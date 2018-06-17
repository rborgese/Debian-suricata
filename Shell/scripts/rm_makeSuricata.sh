#!/bin/bash

# Change directory into suricata uncompressed folder
cd suricata-4.0.4

# Unistall suricata with make uninstall and clean
sudo make uninstall
sudo make clean
