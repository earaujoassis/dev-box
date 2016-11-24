FROM centos:centos7
MAINTAINER Ewerton Assis <earaujoassis@gmail.com>

LABEL Description="Image used for web-based applications in Ruby + Node.js" Version="0.1"
ENV DOCKER true
RUN rpm -Uvh http://dl.fedoraproject.org/pub/epel/7/x86_64/e/epel-release-7-8.noarch.rpm
RUN yum install -y python python-argparse npm wget tar libxslt-devel libxml2-devel postgresql-devel openssl-devel gcc gcc-c++ automake autoconf make curl curl-devel httpd-devel git-all
RUN npm install -g bower gulp

# Install Ruby
ENV RUBY_VERSION 2.3.3
ENV RUBY_VERSION_MAJOR 2.3
ENV RUBY_ARCHIVE ruby-$RUBY_VERSION.tar.gz
ENV RUBY_FOLDER ruby-$RUBY_VERSION
ENV RUBY_DOWNLOAD_URL https://cache.ruby-lang.org/pub/ruby/$RUBY_VERSION_MAJOR/$RUBY_ARCHIVE
ENV RUBY_DOWNLOAD_SHA256 241408c8c555b258846368830a06146e4849a1d58dcaf6b14a3b6a73058115b7
RUN curl -fsSL "$RUBY_DOWNLOAD_URL" -o ruby.tar.gz \
  && echo "$RUBY_DOWNLOAD_SHA256  ruby.tar.gz" | sha256sum -c - \
  && tar xvfvz ruby.tar.gz \
  && rm -f ruby.tar.gz \
  && cd $RUBY_FOLDER \
  && ./configure && make && make install && cd .. && rm -rf $RUBY_FOLDER
RUN gem update; gem update --system; gem install bundler; gem install foreman

RUN mkdir -p /project
WORKDIR /project
