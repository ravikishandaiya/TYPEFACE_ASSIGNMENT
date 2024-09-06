# Dropbox-like Service Documentation

## Overview

The Dropbox-like Service is a simplified file storage application that allows users to upload, retrieve, update, and delete files. It also supports storing metadata for each uploaded file and provides a set of RESTful APIs for managing files.

## Features

- **Upload File API**: Upload files to the server.
- **Read File API**: Retrieve a file using its unique identifier.
- **Update File API**: Update an existing file or its metadata.
- **Delete File API**: Delete a specific file.
- **List Files API**: List all available files and their metadata.

## Technologies

- **Backend Framework**: Django
- **Database**: SQLite (for demo purposes), for production gonna use PSQL
- **File Storage**: Local file system using Docker volumes (AWS S3 for future implementation)

## API Endpoints

### 1. Upload File

- **Endpoint**: `POST /files/upload`
- **Description**: Upload a file to the server.
- **Request Body**:
  - File binary data (multipart/form-data)
- **Response**:
  - `201 Created` on success with a JSON response containing the unique file identifier.
  - `400 Bad Request` if the file is missing or invalid.

### 2. Read File

- **Endpoint**: `GET /files/{fileId}`
- **Description**: Retrieve a file based on its unique identifier.
- **Response**:
  - `200 OK` with the file binary data.
  - `404 Not Found` if the file does not exist.

### 3. Update File

- **Endpoint**: `PUT /files/{fileId}`
- **Description**: Update an existing file or its metadata.
- **Request Body**:
  - New file binary data (multipart/form-data, optional)
  - New filename (optional)
- **Response**:
  - `200 OK` with a JSON response confirming the update.
  - `404 Not Found` if the resource does not exist.
  - `400 Bad Request` if none of above 2 given.

### 4. Delete File

- **Endpoint**: `DELETE /files/{fileId}`
- **Description**: Delete a specific file.
- **Response**:
  - `200 OK` on successful deletion.
  - `404 Not Found` if the file does not exist.

### 5. List Files

- **Endpoint**: `GET /files`
- **Description**: List all files and their metadata.
- **Response**:
  - `200 OK` with a JSON list of file metadata objects.

## Error Handling

- **400 Bad Request**: User input is invalid or missing required data.
- **404 Not Found**: Requested file or resource does not exist.
- **500 Internal Server Error**: Unexpected server error.


## Installation and Setup


**Clone the Repository**

### Using Docker
Navigate to Project Directory



Navigate to Project Directory:
cd dropbox-equivalent-service

	Install Dependencies:
    pip install -r requirements.txt

    Run Migrations:
    python manage.py makemigrations
    python manage.py migrate

    Start the Development Server:
    python manage.py runserver

