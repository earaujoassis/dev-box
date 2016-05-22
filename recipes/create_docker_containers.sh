#!/usr/bin/env bash

echo "\033[92m# Creating Redis container \033[0m"
docker run --name redis-store -d -p 6379:6379 redis
echo "\033[92m# Creating PostgreSQL container \033[0m"
docker run --name postgres-store -d -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=$DATABASE_PASSWORD -p 5432:5432 postgres
echo "\033[92m# Creating MongoDB container \033[0m"
docker run --name mongo-store -d -p 27017:27017 mongo
echo "\033[92m# Creating RabbitMQ container \033[0m"
docker run --name rabbit-store --hostname rabbitmq-default -d -e RABBITMQ_DEFAULT_USER=rabbit -e RABBITMQ_DEFAULT_PASS=$RABBITMQ_PASSWORD -p 5672:5672 rabbitmq
