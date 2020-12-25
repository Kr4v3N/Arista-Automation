#!/usr/bin/env bash


(crontab -l 2>/dev/null; echo "0 5 * * * cd /home/fafa/Documents/OC-Project-6/CfgMngNotification && sudo python3 config.py") | crontab -
