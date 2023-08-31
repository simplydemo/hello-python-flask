# hello-python-flask
python flask 프레임워크로 Web 서비스 프로젝트 템플릿을 구성 합니다.

## Install packages

```
pip install flask
```

## Run
```
python3 app.py
```

## Build Image
```
# for multiple CPU architecture
# docker buildx create --name builder --use
# docker buildx inspect builder
# docker buildx build --platform=linux/arm64,linux/amd64 --builder=builder -t symplesims/hello-python:latest -f ./cicd/docker/Dockerfile .
docker build -t symplesims/hello-python:latest -f ./cicd/docker/Dockerfile .
```

## Run container
```
docker run --rm --name=helloworld -p 8050:8050 symplesims/hello-python:latest
```

## Push to docker hub
```
docker login -u <your_id>

docker push symplesims/hello-python:latest
```

## Kubernetes
Kubernetes 클러스터를 대상으로 hello 애플리케이션을 배포합니다.

### Deploy Pod

```
kubectl apply -f https://raw.githubusercontent.com/simplydemo/hello-python-flask/main/cicd/k8s/hello-po.yaml
```

### Deploy Service

```
kubectl apply -f https://raw.githubusercontent.com/simplydemo/hello-python-flask/main/cicd/k8s/hello-svc-deploy.yaml
```