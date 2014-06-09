#!/usr/bin/env rake

require 'dotenv/tasks'

namespace :nginx do
  desc 'Installs the nginx.conf file'
  task :install do
    require 'yaml'
    require 'erubis'

    projects = YAML.load_file 'config/data/projects.yml'
    template = Erubis::Eruby.new File.read 'config/templates/nginx.conf.erb'
    File.delete('config/nginx.conf') if File.exists? 'config/nginx.conf'
    File.open('config/nginx.conf', 'w+') do |file|
      file.puts template.result projects: projects
    end

    `mv /etc/nginx/sites-available/default /etc/nginx/sites-available/default.backup-#{Time.now.strftime '%Y-%m-%d'}`
    `cp config/nginx.conf /etc/nginx/sites-available/default`
    `/etc/init.d/nginx restart`
  end
end
