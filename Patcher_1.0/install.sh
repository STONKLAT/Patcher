#!/usr/bin/env bash

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

echo 'Installing...\nPlease enter your password, this is needed to integrate the command.'
sudo cp "$SCRIPT_DIR/sources/patcher" /opt/local/bin

echo 'Installation Complete'
