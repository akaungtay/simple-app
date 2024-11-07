# Base Image
FROM python:3.10-alpine
# creating working folder
WORKDIR /code
# setting environmental variable
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
# install software dependencies
RUN apk add --no-cache gcc musl-dev linux-headers
# install App requirement
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
# exposing port of container
EXPOSE 5000
# copy code
COPY . .
#  run Flask
CMD ["flask", "run", "--debug"]