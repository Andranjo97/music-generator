# This is the core code of music generator app

## Requisites
This project uses:
 - python 3.9
 - Docker 20.10

# Get started

## Init venv
```
poetry shell
```

## Install dependencies

```
poetry install
```

## Test

To run tests use
```
pytest .
```

To run coverage use
```
pytest --cov-report=term-missing:skip-covered --cov-config=.coveragerc --cov=app app/tests/
```

## Start application

> **Warning**
> Make sure you have docker installed

Set your environment variables. Check the `.env.example` for references.

To start the application, run
```
docker-compose up --build
```

the api should be running on [http://localhost:8000](http://localhost:8000)
