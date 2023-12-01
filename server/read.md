## Build
docker build -t nfc_demo .

## Run
docker run -p 80:80 nfc_demo:latest

## self-signed certificate and key
openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout nginx-selfsigned.key -out nginx-selfsigned.crt

## Docker Compose
docker-compose up --build