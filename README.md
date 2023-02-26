<h1 align="center"> 99Files API </h1>

 <p align="left">
   <img src="https://img.shields.io/badge/STATUS-%20DEV-green">
</p>


# Introduction
Simple server side exercise, it will be evaluated using a test suite that checks the constraints to assert the business logic is correct and by Onna
engineers on a less objective approach to check overall architecture.

As a lead and only engineer at 99files.com, a website that allows users to upload up to 99 files on their account and download them, your goal is
to provide an application that runs an API where:
Users can upload files to the server
Users can list their files
Users can download files using a unique url

# Schema

    src
    ├── api
    │   ├── app.py
    │   ├── models.py
    │   ├── routes.py
    │   └── services.py
    ├── constants.py
    ├── main.py
    └── tests
# Requirements

- fastapi
- httpx
- uvicorn
- cachetools

# Endpoints
* **POST /files**

Receives a file and stores it in the user's space. If the file already exists, it will be overwritten.

Responses:

    201: On successful upload.
    400: File has been rejected (there are already 99 files).

* **GET /files**

Returns all files on the user's space.

Responses:

    200: On successful call.

* **GET /files/<id>**

Returns the file with the specified ID.

Responses:

    200: On successful call.
    404: If the file is not found.
    429: When the rate limit is hit.

Non-matching endpoints should return a 404 error code. Non-defined methods should return a 405 error code.


# Run
docker build -t app:latest .

docker run -p 80:80 app:latest

# Usage

### /health

    curl -X 'GET' \
      'http://0.0.0.0/health' \
      -H 'accept: application/json'

Response:

    {
      "HealthCheck": "Ok",
      "Version": "0.1.0"
    }

### /files

    curl -X 'POST' \
      'http://0.0.0.0/files' \
      -H 'accept: application/json' \
      -H 'Content-Type: application/json' \
      -d '{
      "id": "2",
      "name": "file_2.txt",
      "url": "url_2"
    }'

    curl -X 'POST' \
      'http://0.0.0.0/files' \
      -H 'accept: application/json' \
      -H 'Content-Type: application/json' \
      -d '{
      "id": "1",
      "name": "file_1.txt",
      "url": "url_1"
    }'

Response:

    [
      {
        "id": "1",
        "name": "file_1.txt",
        "ur": "url_1"
      },
      {
        "id": "2",
        "name": "file_2.txt",
        "ur": "url_2"
      }
    ]

### /files/{id_file}

    curl -X 'GET' \
      'http://0.0.0.0/files/1' \
      -H 'accept: application/json'

Response

    {
      "file": "file_1.txt"
    }


# Run Tests

    python -m unittest discover tests

# Comments:

The data are not persistent. To avoid data loss if the service is stopped, the data should be indexed in a database.
