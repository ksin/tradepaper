#!/bin/sh

# This is for a local Django dev environment for trade-paper on a Mac,
# but it's not robust so don't be surprised if you encounter issues

# More for reference than for an automated spin-up

ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

brew install pyenv

brew install postgres

git clone https://github.com/yyuu/pyenv-virtualenv.git ~/.pyenv/plugins/pyenv-virtualenv

echo 'eval "$(pyenv init -)"' >> ~/.bash_profile

echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bash_profile

# in parent folder of git directory
mkdir static
mkdir media
sudo ln -s tradepaper/fabfile.py fabfile.py

pyenv install 2.7.6

pyenv install 3.4.3

git clone git@github.com:ebierman/tradepaper.git

pyenv virtualenv 2.7.6 fabric

pyenv virtualenv 3.4.3 paper

#in same directory as manage.py
pyenv local paper
pip install -r requirements.txt --allow-all-external

#in parent of git directory
pyenv local fabric

