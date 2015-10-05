#!/usr/bin/env bash

echo "\033[92m# Creating redis-store \033[0m"
docker run --name redis-store -d -p 6379:6379 redis
echo "\033[92m# Creating postgres-store \033[0m"
docker run --name postgres-store -d -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=$DATABASE_PASSWORD -p 5432:5432 postgres
