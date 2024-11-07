# simple-app

Eample from [docker](https://docs.docker.com/compose/gettingstarted/)

## Commands
### Building & Running Image

```
docker pull python:3.10-alpine

docker build -t app:v1.0 . 

docker image ls 

docker run -it -p 6379:6379 redis:alpine

docker ps

docker container ls

docker inspect xxxx

# add the gateway IP or container IP

docker run -it -p 8000:8050 -e REDISIP="172.17.0.1" -e PORT=8050 app:v1.0

```
### Docker Compose

```
docker compose -f ./compose.yaml up -d

docker compose ls

docker compose ps

docker compose logs

docker compose stats

docker compose down

docker compose -f ./compose-watch.yaml up --watch

docker compose logs web

docker network ls

```

### Check Redis Server
```
nc -v localhost 6379

PING

SET mykey "Hello, Redis!"

GET mykey

```
