FROM centos:centos7
MAINTAINER Ewerton Assis <earaujoassis@gmail.com>

LABEL Description="Image used for web-based applications in Ruby + Node.js" Version="0.1"
ENV DOCKER true
RUN rpm -Uvh http://dl.fedoraproject.org/pub/epel/7/x86_64/e/epel-release-7-8.noarch.rpm
RUN yum install -y python python-argparse npm wget tar libxslt-devel libxml2-devel postgresql-devel openssl-devel gcc gcc-c++ automake autoconf make curl curl-devel httpd-devel
RUN npm install -g bower gulp

# Install Ruby
ENV RUBY_VERSION_MAJOR 2.3
ENV RUBY_VERSION 2.3.1
ENV RUBY_ARCHIVE ruby-$RUBY_VERSION.tar.gz
RUN wget https://cache.ruby-lang.org/pub/ruby/$RUBY_VERSION_MAJOR/$RUBY_ARCHIVE
RUN tar xvfvz $RUBY_ARCHIVE
RUN rm -f $RUBY_ARCHIVE
RUN cd ruby-$RUBY_VERSION; ./configure; make; make install; cd ..; rm -rf ruby-$RUBY_VERSION
RUN gem update; gem update --system; gem install bundler; gem install foreman

RUN mkdir -p /project
WORKDIR /project
