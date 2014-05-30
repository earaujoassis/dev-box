# -*- mode: ruby -*-
# vi: set ft=ruby :

ROOT_DIR = File.expand_path File.dirname(__FILE__)
LOCAL_VAGRANTFILE = File.join ROOT_DIR, 'Vagrantfile.local'

# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box = "dev-box"
  config.vm.box_url = "file://C:/Users/Ewerton/Dropbox/earaujoassis/vm-box/vagrant-ubuntu64.box"
  config.vm.hostname = "local.ewerton-araujo.com"
  config.vm.network "private_network", ip: "192.168.0.77"

  config.vm.provider "virtualbox" do |vb|
    vb.memory = 1024
    vb.cpus = 2
  end
end

# Load local Vagrant configuration overrides
if File.exists? LOCAL_VAGRANTFILE
  load LOCAL_VAGRANTFILE
end
