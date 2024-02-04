#!/bin/bash
rm -r /etc/xdxl
apt update && apt upgrade -y
apt install python3 python3-pip -y
apt install sqlite3 -y
mkdir -p /etc/xdxl
cd /etc/xdxl
git clone https://github.com/zhets/xolpanel.git
cd xolpanel
mv xolpanel.service /etc/systemd/system/
pip3 install -r requirements.txt
pip install pillow
pip install speedtest-cli
domain=$(cat /etc/xray/domain)
clear
echo -e "  INSTALL BOT CREATE SSH VIA TELEGRAM"
echo -e " Masukan Info Bot Kamu ! "
read -e -p "[*] Input Your Token Bot : " token
read -e -p "[*] Input Your Id Telegram : " admin
echo -e ADMIN='"'$admin'"' >> /etc/xdxl/xolpanel/var.txt
echo -e BOT_TOKEN='"'$token'"' >> /etc/xdxl/xolpanel/var.txt
echo -e DOMAIN='"'$domain'"' >> /etc/xdxl/xolpanel/var.txt

systemctl daemon-reload
systemctl start xolpanel
systemctl enable xolpanel
systemctl restart xolpanel
clear
echo -e ""
echo " Installations complete, type /menu on your bot "
