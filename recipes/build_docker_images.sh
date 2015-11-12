#!/usr/bin/env bash

echo "Building images at: /vagrant/docker"
cd /vagrant/docker && docker build -t earaujoassis/devbox .
