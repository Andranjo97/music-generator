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

To start the application, run
```
docker-compose up --build
```

the api should be running in [http://localhost:8000](http://localhost:8000)
