# Base Image
FROM python:3.10-alpine
# creating working folder
WORKDIR /code
# setting environmental variable
ENV PORT=8050
ENV REDISIP="redis"
# install software dependencies
# RUN apk add --no-cache gcc musl-dev linux-headers
# install App requirement
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
# exposing port of container
EXPOSE 8050
# copy code
COPY . .
#  run Flask
CMD ["python", "app.py"]