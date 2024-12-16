# API-template-Python

## Setup

Install the `requiremets.txt` files to get up an running.

## Local

**Using uvicorn**:
```
uvicorn app.api:app --host 0.0.0.0 --port 8000 --reload
```

**Using FastAPI**:
```
fastapi dev .\app\api.py
```

## Docker
To build the docker image:
```
docker build --no-cache -t {docker-image-name}:{version} .
```

To execute the docker container:
```
docker run --env-file ./path/to/.env -p 8000:8000 -d --rm {docker-image-name}:{version}  
```

## Contribution

Check the *RULES.md* file in girhub folder to understand how to contribute.