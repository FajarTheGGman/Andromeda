#!/usr/bin/bash

# installing package

echo "[!] Installing Package"
sleep(1)
apt-get update && apt-get upgrade -y
apt-get install python -y
pip install urllib3 tkinter
echo "Done :) "
sleep(0.5)
echo "[+] Running Program..."
sleep(1)
python run.py
