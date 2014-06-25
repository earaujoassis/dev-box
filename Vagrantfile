# -*- mode: ruby -*-
# vi: set ft=ruby :

ROOT_DIR = File.expand_path File.dirname(__FILE__)
LOCAL_VAGRANTFILE = File.join ROOT_DIR, 'Vagrantfile.local'

# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box = "ubuntu/trusty64"
  config.vm.hostname = "local.ewerton-araujo.com"
  config.vm.network "private_network", ip: "192.168.66.88"
  config.vm.provision "shell", path: "config/provision.sh"

  config.vm.provider "virtualbox" do |vb|
    vb.memory = 2048
    vb.cpus = 2
  end
end

# Load local Vagrant configuration overrides
if File.exists? LOCAL_VAGRANTFILE
  load LOCAL_VAGRANTFILE
end
