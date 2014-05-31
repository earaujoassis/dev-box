#!/usr/bin/env rake

require 'dotenv/tasks'

namespace :nginx do 
  desc 'Installs the nginx.conf file'
  task :install do
    `mv /etc/nginx/sites-available/default /etc/nginx/sites-available/default.backup-#{Time.now.strftime '%Y-%m-%d'}`
    `cp config/nginx.conf /etc/nginx/sites-available/default`
    `/etc/init.d/nginx restart`
  end
end
