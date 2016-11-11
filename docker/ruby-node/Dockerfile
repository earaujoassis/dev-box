FROM centos:centos6
MAINTAINER Ewerton Assis <earaujoassis@gmail.com>

LABEL Description="Image used for web-based applications in DevBox" Version="0.1"
ENV DEVBOX_DOCKER true
RUN rpm -Uvh http://download.fedoraproject.org/pub/epel/6/i386/epel-release-6-8.noarch.rpm
RUN yum install -y python python-argparse npm wget tar libxslt-devel libxml2-devel postgresql-devel openssl-devel gcc gcc-c++ automake autoconf make curl curl-devel httpd-devel
RUN npm install -g bower gulp
RUN wget https://cache.ruby-lang.org/pub/ruby/2.3/ruby-2.3.1.tar.gz
RUN tar xvfvz ruby-2.3.1.tar.gz
RUN rm -f ruby-2.3.1.tar.gz
RUN cd ruby-2.3.1; ./configure; make; make install; cd ..; rm -rf ruby-2.3.1
RUN gem update; gem update --system; gem install bundler
RUN mkdir -p /project
