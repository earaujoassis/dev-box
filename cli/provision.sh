#!/usr/bin/env bash

sudo apt-get update && sudo apt-get upgrade -y
sudo apt-get install -y build-essential git-core curl htop zsh python-dev zlib1g-dev libssl-dev
sudo touch /etc/environment
touch $HOME/.profile
echo 'LC_ALL="en_US.UTF-8"' | sudo tee -a /etc/environment

sudo apt-get install -y build-essential git-core zsh curl htop python-dev libevent-dev libffi-dev php5-cli php5-curl

curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.31.0/install.sh | sh
wget -O- https://toolbelt.heroku.com/install-ubuntu.sh | sh
sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv EA312927
echo "deb http://repo.mongodb.org/apt/debian wheezy/mongodb-org/3.0 main" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.0.list
sudo apt-get update
sudo apt-get install -y --force-yes mongodb-org
sudo service mongod start

wget https://bootstrap.pypa.io/get-pip.py
sudo python get-pip.py
pip install --user -I pip setuptools virtualenv virtualenvwrapper
rm -f get-pip.py
echo 'export WORKON_HOME=$HOME/.virtualenvs' >> $HOME/.profile
grep -q -F 'dsmgr-localbin' $HOME/.profile || echo 'export PATH="$HOME/bin:$HOME/.local/bin:$PATH" # dsmgr-localbin' >> $HOME/.profile
grep -q -F 'dsmgr-venvwrapper' $HOME/.profile || echo 'source $HOME/.local/bin/virtualenvwrapper.sh # dsmgr-venvwrapper' >> $HOME/.profile
source /home/vagrant/.zshrc

sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt/ `lsb_release -cs`-pgdg main" >> /etc/apt/sources.list.d/pgdg.list'
wget -q https://www.postgresql.org/media/keys/ACCC4CF8.asc -O - | sudo apt-key add -
sudo apt-get update
sudo apt-get install -y --force-yes postgresql postgresql-contrib

gpg --keyserver hkp://keys.gnupg.net --recv-keys 409B6B1796C275462A1703113804BB82D39DC0E3
curl -sSL https://get.rvm.io | bash -s stable --ruby
echo progress-bar >> ~/.curlrc
gem install bundler
sudo usermod -aG vboxsf vagrant
curl -sSL https://get.docker.com/ | sh
sudo usermod -aG docker vagrant
source /home/vagrant/.zshrc

curl -OL https://github.com/robbyrussell/oh-my-zsh/raw/master/tools/install.sh
bash install.sh
rm -f install.sh

mkdir -p $HOME/.local
cd $HOME
wget https://www.python.org/ftp/python/2.7.8/Python-2.7.8.tar.xz
tar -xf $HOME/Python-2.7.8.tar.xz
cd $HOME/Python-2.7.8 && ./configure --with-zlib --prefix=$HOME/.local && make && make install
cd $HOME && rm -rf $HOME/Python-2.7.8
rm -f $HOME/Python-2.7.8.tar.xz
echo 'source ~/.profile' >> $HOME/.zshrc

sudo apt-get autoremove -y
sudo apt-get autoclean -y

echo ''
echo 'SYSTEM IS ABOUT TO SHUTDOWN'
echo 'PLEASE BOOT IT UP AGAIN: `vagrant up`'
shutdown -h now
