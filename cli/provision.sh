#!/usr/bin/env bash

sudo apt-get update && sudo apt-get upgrade -y
sudo apt-get install -y build-essential git-core curl htop zsh python-dev
echo 'LC_ALL="en_US.UTF-8"' | sudo tee /etc/environment

gpg --keyserver hkp://keys.gnupg.net --recv-keys 409B6B1796C275462A1703113804BB82D39DC0E3
curl -sSL https://get.rvm.io | bash -s stable --ruby
echo progress-bar >> ~/.curlrc
gem install bundler
sudo usermod -aG vboxsf vagrant
curl -sSL https://get.docker.com/ | sh
sudo usermod -aG docker vagrant

sudo apt-get autoremove -y
sudo apt-get autoclean -y

curl -OL https://github.com/robbyrussell/oh-my-zsh/raw/master/tools/install.sh
bash install.sh
rm -f install.sh

echo ''
echo 'SYSTEM IS ABOUT TO SHUTDOWN'
echo 'PLEASE BOOT IT UP AGAIN: `vagrant up`'
shutdown -h now
