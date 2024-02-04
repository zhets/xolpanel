#!/bin/bash
# ================================
# // Arthur : XDXL STORE
# // From : North Lampung ( Indonesia )
# // Channel : t.me/xdxl_vpn
# // Group : t.me/vpn_storeid
# // Contact : t.me/xdxl_store
# ==================================
# Note :
# Jangan lupa makan buat yg colong bot nya hehe

domain=$(cat /etc/xray/domain)
SYSTEM=systemctl
SYSTEMD=/etc/systemd/system
xd=xolpanel
bot=/etc/xdxl
if [ -d $bot ]; then
    rm -rf $bot
    mkdir -p $bot
fi
if [ -e $SYSTEMD/$xd.service ]; then
    $SYSTEM stop $xd
    $SYSTEM disable $xd
    rm -rf $SYSTEMD/$xd.service
    $SYSTEM daemon-reload
fi
apt update && apt upgrade -y
apt install python3 python3-pip -y
apt install sqlite3 -y
cd $bot
git clone https://github.com/zhets/${xd}.git
cd $xd
rm install.sh uninstall.sh
mv ${xd}.service $SYSTEMD/
pip3 install -r requirements.txt
pip install pillow
pip install speedtest-cli
clear
echo -e "==================================="
echo -e "  Simple Bot Telegram create SSH"
echo -e "==================================="
echo -e " Masukan Info Bot Kamu ! "
read -e -p "[*] Masukan Token Bot kamu : " token
read -e -p "[*] Masukan Id Telegram Kamu : " admin
echo -e ADMIN='"'$admin'"' >> $bot/$xd/var.txt
echo -e BOT_TOKEN='"'$token'"' >> $bot/$xd/var.txt
echo -e DOMAIN='"'$domain'"' >> $bot/$xd/var.txt
cd
$SYSTEM daemon-reload
$SYSTEM start $xd
$SYSTEM enable $xd
$SYSTEM restart $xd
clear
echo -e ""
echo " Installations complete, type /menu on your bot "
rm -rf /root/install.sh
