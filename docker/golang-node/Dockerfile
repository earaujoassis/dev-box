FROM centos:centos7
MAINTAINER Ewerton Assis <earaujoassis@gmail.com>

LABEL Description="Image used for web-based applications in Go + Node.js" Version="0.1"
ENV DOCKER true
RUN rpm -Uvh http://dl.fedoraproject.org/pub/epel/7/x86_64/e/epel-release-7-8.noarch.rpm
RUN yum install -y python python-argparse npm wget tar libxslt-devel libxml2-devel postgresql-devel openssl-devel gcc gcc-c++ automake autoconf make curl curl-devel httpd-devel git-all
RUN npm install -g bower gulp

# Install Go
ENV GOLANG_VERSION 1.7.3
ENV GOLANG_DOWNLOAD_URL https://golang.org/dl/go$GOLANG_VERSION.linux-amd64.tar.gz
ENV GOLANG_DOWNLOAD_SHA256 508028aac0654e993564b6e2014bf2d4a9751e3b286661b0b0040046cf18028e
RUN curl -fsSL "$GOLANG_DOWNLOAD_URL" -o golang.tar.gz \
  && echo "$GOLANG_DOWNLOAD_SHA256  golang.tar.gz" | sha256sum -c - \
  && tar -C /usr/local -xzf golang.tar.gz \
  && rm golang.tar.gz
ENV GOPATH /go
ENV PATH $GOPATH/bin:/usr/local/go/bin:$PATH
RUN mkdir -p "$GOPATH/src" "$GOPATH/bin" && chmod -R 777 "$GOPATH"
RUN go get github.com/mattn/goreman
RUN go get github.com/tools/godep

WORKDIR /go
