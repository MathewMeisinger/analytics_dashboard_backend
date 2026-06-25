# Telecom Analytics API Architecture

## Overview

The Telecom Analytics API is a RESTful backend service built with FastAPI that provides access to Call Detail Record (CDR) data stored in MongoDB Atlas.

The API acts as the communication layer between the Streamlit dashboard and the MongoDB database.

```
                Streamlit Dashboard
                        │
                        │ HTTP / JSON
                        ▼
                 FastAPI Backend
                        │
                        ▼
                 Service Layer
                        │
                        ▼
                  MongoDB Atlas
```

## Project Structure

```
app/
│
├── config/
│     database.py
│
├── models/
│     cdr.py
│
├── routers/
│     cdr.py
│     analytics.py
│     metadata.py
│     auth.py
│
├── services/
│     cdr_service.py
│     analytics_service.py
│     metadata_service.py
│     auth_service.py
│
└── main.py
```

## Responsibilities

### Routers

Receive HTTP requests and return responses.

### Services

Contain business logic and MongoDB queries.

### Models

Validate request and response data.

### Config

Manage database connections and environment variables.