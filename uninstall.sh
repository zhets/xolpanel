#!/bin/sh

SYSTEM=systemctl
BOT=/etc/xdxl

if [ `id -u` != "0" ]; then
    echo "Error at uninstallation, please run uninstaller as root"
    exit 1
fi

echo "Uninstalling Bot create SSH..."
if [ -f /etc/systemd/system/xolpanel.service ]; then
    $SYSTEM stop xolpanel.service
    $SYSTEM disable xolpanel.service
    rm $SYSTEM/xolpanel.service
    $SYSTEM daemon-reload
fi
if [ -f $BOT/xolpanel ]; then
    rm -r $BOT/xolpanel
fi
if [ -d $CONFIGS ]; then
    rm -rf $CONFIGS
fi
echo "Uninstall Bot create SSH completed"￼
