#!/bin/bash

sudo apt-get install python3-venv
sudo apt-get install mysql-server
python3 -m venv ./venv
source ./venv/bin/activate
pip install -r requirements.txt
