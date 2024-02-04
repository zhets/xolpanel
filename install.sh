#!/bin/bash
rm -r /etc/xdxl
mkdir -p /etc/xdxl
domain=$(cat /etc/xray/domain)
SYSTEM=systemctl
xd=xolpanel
bot=/etc/xdxl
apt update && apt upgrade -y
apt install python3 python3-pip -y
apt install sqlite3 -y
cd /etc/xdxl
git clone https://github.com/zhets/${xd}.git
cd $xd
mv ${xd}.service /etc/systemd/system/
pip3 install -r requirements.txt
pip install pillow
pip install speedtest-cli
clear
echo -e "  INSTALL BOT CREATE SSH VIA TELEGRAM"
echo -e " Masukan Info Bot Kamu ! "
read -e -p "[*] Input Your Token Bot : " token
read -e -p "[*] Input Your Id Telegram : " admin
echo -e ADMIN='"'$admin'"' >> $bot/$xd/var.txt
echo -e BOT_TOKEN='"'$token'"' >> $bot/$xd/var.txt
echo -e DOMAIN='"'$domain'"' >> $bot/$xd/var.txt

$SYSTEM daemon-reload
$SYSTEM start $xd
$SYSTEM enable $xd
$SYSTEM restart $xd
clear
echo -e ""
echo " Installations complete, type /menu on your bot "
