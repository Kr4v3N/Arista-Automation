#!/usr/bin/env bash

apt-get install uml-utilities
modprobe tun
tunctl
ifconfig tap0 10.10.10.100 netmask 255.255.255.0 up
sleep 2
ifconfig tap0
