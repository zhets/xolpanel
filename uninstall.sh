#!/bin/sh

SYSTEM=systemctl
BOT=/etc/xdxl
xd=xolpanel

if [ `id -u` != "0" ]; then
    echo "Error at uninstallation, please run uninstaller as root"
    exit 1
fi

echo "Uninstalling Bot create SSH..."
if [ -f /etc/systemd/system/$xd.service ]; then
    $SYSTEM stop $xd
    $SYSTEM disable $xd
    rm $SYSTEM/$xd.sevice
    $SYSTEM daemon-reload
fi
if [ -d $BOT/$xd ]; then
    rm -rf $BOT/$xd
fi
clear
echo -e ""
echo "Uninstall Bot create SSH completed"￼
