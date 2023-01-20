# This is the core code of music generator app

## Versions
This project uses:
 - python 3.9
 - Docker 20.10

# Get started

## Install dependencies

```
pip install -r requirements.txt
```

## Test

To run tests use
```
pytest .
```

To run coverage use
```
coverage report -m
```

## Start application

> **Warning**
> Make sure you have docker installed

To start the application, first create a docker image
```
docker build -t music-generator -f Dockerfile.local .
```

and then start your docker container with
```
docker run --name music-generator -p 8000:80 music-generator
```
the api should be running in [http://localhost:8000](http://localhost:8000)
