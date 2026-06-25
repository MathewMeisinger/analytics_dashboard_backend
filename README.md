# PineVox Analytics API

![FastAPI](https://img.shields.io/badge/FastAPI-0.138-009688?logo=fastapi)
![Python](https://img.shields.io/badge/Python-3.12+-3776AB?logo=python)
![MongoDB](https://img.shields.io/badge/MongoDB-Atlas-47A248?logo=mongodb)
![JWT](https://img.shields.io/badge/Auth-JWT-blue)
![Render](https://img.shields.io/badge/Hosted%20on-Render-46E3B7)

REST API providing secure access to Call Detail Record (CDR) analytics
for the PineVox Analytics Dashboard.

```{=html}
</p>
```

------------------------------------------------------------------------

# Overview

The PineVox Analytics API is a FastAPI-based backend responsible for
serving analytics and call record data to the Streamlit Analytics
Dashboard.

The API exposes secure REST endpoints that provide dashboard metrics,
regional analytics, call activity trends, metadata, and paginated call
records. Authentication is implemented using JSON Web Tokens (JWT), with
Role-Based Access Control (RBAC) protecting all sensitive endpoints.

MongoDB Atlas is used as the primary data store while the application is
deployed to Render.

------------------------------------------------------------------------

# Features

-   RESTful API built with FastAPI
-   MongoDB Atlas integration
-   JWT Authentication
-   Role-Based Access Control (RBAC)
-   Password hashing using bcrypt
-   Secure protected endpoints
-   Dashboard analytics endpoints
-   Metadata endpoints
-   Paginated Call Detail Records (CDR)
-   Custom exception handling
-   Automatic OpenAPI documentation
-   Swagger UI
-   ReDoc documentation
-   Cloud deployment with Render

------------------------------------------------------------------------

# System Architecture

``` text
                Streamlit Dashboard
                        │
            HTTPS + Bearer JWT Token
                        │
                        ▼
                 PineVox Analytics API
          ┌─────────────────────────────┐
          │ Authentication              │
          │ Analytics Services          │
          │ Metadata Services           │
          │ CDR Services                │
          └──────────────┬──────────────┘
                         │
                         ▼
                  MongoDB Atlas
```

------------------------------------------------------------------------

# Technology Stack

  Technology         Purpose
  ------------------ -------------------------------
  Python             Backend language
  FastAPI            REST API framework
  MongoDB Atlas      Cloud database
  PyMongo            Database driver
  JWT                Authentication
  Passlib / bcrypt   Password hashing
  Pydantic           Request & response validation
  Uvicorn            ASGI server
  Render             Deployment platform

------------------------------------------------------------------------

# Authentication

Authentication is implemented using JSON Web Tokens (JWT).

After successful login, the API returns a signed JWT access token.

`POST /auth/login`

The client includes the token on every protected request using the
`Authorization: Bearer <token>` header.

------------------------------------------------------------------------

# Role-Based Access Control

  Role      Permissions
  --------- -----------------------------------------
  Admin     Full access to all protected endpoints
  Analyst   Read-only access to analytics endpoints

------------------------------------------------------------------------

# API Endpoints

## Authentication

  Method   Endpoint       Description
  -------- -------------- ----------------------------
  POST     /auth/login    Authenticate user
  POST     /auth/signup   Register user (optional)
  GET      /auth/me       Current authenticated user

## Analytics

  Method   Endpoint                            Description
  -------- ----------------------------------- ------------------------
  GET      /analytics/summary                  Dashboard KPIs
  GET      /analytics/calls-by-hour            Hourly call activity
  GET      /analytics/calls-by-day             Daily call activity
  GET      /analytics/calls-by-city            Calls grouped by city
  GET      /analytics/cost-by-city             Cost analysis
  GET      /analytics/call-type-distribution   Incoming vs outgoing
  GET      /analytics/top-callers              Highest volume callers
  GET      /analytics/call-records             Filtered call records

## Metadata

  Method   Endpoint    Description
  -------- ----------- -------------------------
  GET      /metadata   Dashboard filter values

## Call Detail Records

  Method   Endpoint   Description
  -------- ---------- -----------------------
  GET      /cdr       Paginated CDR records

Supports filtering by city, caller number, receiver number, date range
and pagination.

------------------------------------------------------------------------

# Project Structure

``` text
app/
├── auth/
├── config/
├── models/
├── routers/
├── services/
├── exceptions.py
└── main.py

docs/
├── api_endpoints.md
├── architecture.md
└── database_schema.md
```

------------------------------------------------------------------------

# Installation

``` bash
git clone <repository-url>
cd <repository>
python -m venv .venv
```

Windows:

``` bash
.venv\Scripts\activate
```

Install dependencies:

``` bash
pip install -r requirements.txt
```

------------------------------------------------------------------------

# Environment Variables

``` env
MONGO_URI=
DATABASE_NAME=
COLLECTION_NAME=
JWT_SECRET_KEY=
JWT_ALGORITHM=HS256
JWT_EXPIRE_MINUTES=30
```

------------------------------------------------------------------------

# Running the API

``` bash
uvicorn app.main:app --reload
```

Swagger UI: `/docs`

ReDoc: `/redoc`

------------------------------------------------------------------------

# Deployment

The API is deployed to Render using environment variables for
configuration and MongoDB Atlas as the database.

------------------------------------------------------------------------

# Security

-   Password hashing with bcrypt
-   JWT authentication
-   Role-Based Access Control
-   Pydantic request validation
-   Environment variable configuration

------------------------------------------------------------------------

# Documentation

Additional technical documentation is available in the `docs/`
directory.

------------------------------------------------------------------------

# Future Improvements

-   Refresh tokens
-   Token revocation
-   Docker support
-   Unit and integration tests
-   Rate limiting
-   Audit logging
-   GitHub Actions CI/CD

------------------------------------------------------------------------

# Frontend

This API is consumed by the companion Streamlit Analytics Dashboard.

------------------------------------------------------------------------

# Author

**Mathew Meisinger**

Software Engineer \| Data Analyst \| AI Enthusiast
