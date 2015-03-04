#!/bin/sh

cd ~/Documents/Website\ HTML\ and\ CSS/tradepaper-dev/tradepaper
pip install -r requirements.txt --allow-all-external
./manage.py migrate
./manage.py runserver
