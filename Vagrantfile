# -*- mode: ruby -*-
# vi: set ft=ruby :

ROOT_DIR = File.expand_path File.dirname(__FILE__)
LOCAL_VAGRANTFILE = File.join ROOT_DIR, 'Vagrantfile.local'

Vagrant.configure(2) do |config|
  config.vm.hostname = "dev-box"
  config.vm.box = "ubuntu/vivid64"
  config.vm.network "private_network", ip: "192.168.44.88"
  config.ssh.forward_agent = true

  config.vm.network :forwarded_port, guest: 5000, host: 5000
  config.vm.network :forwarded_port, guest: 5050, host: 5050
  config.vm.network :forwarded_port, guest: 8000, host: 8000
  config.vm.network :forwarded_port, guest: 8080, host: 8080
  config.vm.network :forwarded_port, guest: 27017, host: 27017 # MongoDB
  config.vm.network :forwarded_port, guest: 6379, host: 6379   # Redis
  config.vm.network :forwarded_port, guest: 5432, host: 5432   # Postgres

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
