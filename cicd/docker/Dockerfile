FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt /app
COPY app.py /app
COPY static /app/static
COPY templates /app/templates

RUN pip3 install -r requirements.txt
RUN chmod +x /app/app.py

CMD ["python3", "app.py"]

## docker build -t symplesims/helloworld:latest -f ./cicd/docker/Dockerfile .
## docker run --name=helloworld -p 8050:8050 symplesims/helloworld:latest
