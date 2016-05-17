# -*- mode: ruby -*-
# vi: set ft=ruby :

ROOT_DIR = File.expand_path File.dirname(__FILE__)
LOCAL_VAGRANTFILE = File.join ROOT_DIR, 'Vagrantfile.local'

Vagrant.configure(2) do |config|
  config.vm.hostname = "dev-box"
  config.vm.box = "ubuntu/vivid64"
  config.vm.network "private_network", ip: "192.168.44.88"
  config.ssh.forward_agent = true

  config.vm.network :forwarded_port, guest: 27017, host: 27017  # MongoDB
  config.vm.network :forwarded_port, guest: 6379,  host: 6379   # Redis
  config.vm.network :forwarded_port, guest: 5432,  host: 5432   # Postgres
  config.vm.network :forwarded_port, guest: 5672,  host: 5672   # RabbitMQ

  # Applications binds

  config.vm.network :forwarded_port, guest: 33507, host: 33507
  config.vm.network :forwarded_port, guest: 5000,  host: 5000
  config.vm.network :forwarded_port, guest: 7654,  host: 7654
  config.vm.network :forwarded_port, guest: 8000,  host: 8000

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

  config.vm.provision "shell", path: "cli/provision.sh", privileged: false
end

# Load local Vagrant configuration overrides
if File.exists? LOCAL_VAGRANTFILE
  load LOCAL_VAGRANTFILE
end
