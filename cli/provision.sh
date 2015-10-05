#!/usr/bin/env bash

gpg --keyserver hkp://keys.gnupg.net --recv-keys 409B6B1796C275462A1703113804BB82D39DC0E3
curl -sSL https://get.rvm.io | bash -s stable --ruby
echo progress-bar >> ~/.curlrc
gem install bundler
sudo usermod -aG vboxsf vagrant
curl -sSL https://get.docker.com/ | sh
sudo usermod -aG docker vagrant
