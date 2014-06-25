#!/bin/bash

set -e

if [[ $EUID -ne 0 ]]; then
  echo "This script must be run as root" 1>&2
  exit 1
fi

echo -e "vm.swappiness=0" | sudo tee -a /etc/sysctl.conf
mkdir -p ~/tmp

sudo apt-get update
sudo apt-get install -y \
  curl git-core build-essential zlib1g-dev libreadline-dev libssl-dev htop

sudo apt-get install -y nginx

sudo apt-get install -y postgresql postgresql-contrib postgresql-server-dev-all
sudo -u postgres psql -c "create user vagrant inherit login superuser"
sudo -u postgres psql -c "alter user vagrant with password 'vagrant'"
sudo -u postgres psql -c "create user root inherit login superuser"

#export DEBIAN_FRONTEND=noninteractive
#sudo apt-get install -y -q mysql-server
#mysqladmin -u root password vagrant

sudo apt-get install -y scons
cd ~/tmp
git clone https://github.com/mongodb/mongo.git
cd mongo
git checkout r2.6.3
scons all
sudo scons install
sudo groupadd mongodb
sudo useradd mongodb -d /var/lib/mongodb -s /bin/false -c "Mongodb user" -g mongodb
sudo cp /vagrant/config/mongod.conf /etc/mongod.conf
sudo chown root:root /etc/mongod.conf
sudo cp /vagrant/config/mongodb /etc/init.d/mongodb
sudo chmod 755 /etc/init.d/mongodb
sudo chown root:root /etc/init.d/mongodb

cd ~/tmp
git clone https://github.com/antirez/redis.git
cd redis
git checkout 2.8.11
make && sudo make install
cd utils
echo -ne '\n' | sudo ./install_server.sh

cd ~/tmp
rm -rf /tmp/ruby-build
git clone https://github.com/sstephenson/ruby-build.git
cd ruby-build
./install.sh
ruby-build 2.1.2 /usr/local/
gem pristine --all
gem install bundler --no-ri --no-rdoc

cd ~/tmp
git clone https://github.com/joyent/node.git
cd node
git checkout v0.10.29
./configure && make && sudo make install
sudo npm -g install grunt gulp bower mocha coffee-script

rm -rf ~/tmp/*
sudo apt-get autoremove
sudo apt-get clean
