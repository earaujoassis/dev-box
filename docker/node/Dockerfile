FROM centos:centos7
MAINTAINER Ewerton Assis <earaujoassis@gmail.com>

LABEL Description="Image used for web-based applications in Node.js" Version="0.1"
ENV DOCKER true
RUN rpm -Uvh http://dl.fedoraproject.org/pub/epel/7/x86_64/e/epel-release-7-8.noarch.rpm
RUN yum install -y python python-argparse npm wget tar libxslt-devel libxml2-devel postgresql-devel openssl-devel gcc gcc-c++ automake autoconf make curl curl-devel httpd-devel git-all
RUN npm install -g bower gulp foreman
