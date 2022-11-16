# Fully-automatic-LINE-commercial-robot

## About this project

## How to use
1. use Dockerfile build env image
```bash
docker build -t rakunabe .
```
2. create project file
```bash
mkdir app.py
```
3. run your project in the container 
```bash
docker run --name rakunabe -p 5002:5002 --restart=always -v /root/Fully-automatic-LINE-commercial-robot:/app -d rakunabe
```