# -*- mode: ruby -*-
# vi: set ft=ruby :

ROOT_DIR = File.expand_path File.dirname(__FILE__)
LOCAL_VAGRANTFILE = File.join ROOT_DIR, 'Vagrantfile.local'

Vagrant.configure(2) do |config|
  config.vm.hostname = "dev-box"
  config.vm.box = "ubuntu/vivid64"
  config.vm.network "private_network", ip: "192.168.44.88"

  config.vm.provider :virtualbox do |vb|
    vb.customize [
      "modifyvm", :id,
      "--cpuexecutioncap", "75",
      "--memory", "768",
      "--cpus", "2"
    ]

    vb.customize [
      "setextradata", :id,
      "VBoxInternal2/SharedFoldersEnableSymlinksCreate/vagrant", "1"
    ]
  end

  config.vm.provision "shell", inline: <<-SHELL
     sudo apt-get update && sudo apt-get upgrade -y
     sudo apt-get install -y curl htop zsh
     sudo apt-get autoremove -y
     sudo apt-get autoclean -y
     echo 'LC_ALL="en_US.UTF-8"' >> /etc/environment
     shutdown -h now
  SHELL
end

# Load local Vagrant configuration overrides
if File.exists? LOCAL_VAGRANTFILE
  load LOCAL_VAGRANTFILE
end
