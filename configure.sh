#!/bin/bash

# Create configuration file from templates

CORE_DIR='api/keehost_core'
LOGIN_DIR='login/keehost_login'

echo "[+] Removing last configs .."
rm -rf config/
mkdir -p config/

# Keehost Main Service
cp -rf $CORE_DIR/config/config.tpl.py $CORE_DIR/config/config.py
ln $CORE_DIR/config/config.py config/api_config.py

# Keehost login service
cp -rf $LOGIN_DIR/config/config.tpl.py $LOGIN_DIR/config/config.py
ln $LOGIN_DIR/config/config.py config/login_config.py


echo "[+] Done !"
