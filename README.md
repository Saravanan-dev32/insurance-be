# Insurance API with Python and Flask

A RESTful API service for managing insurance policies built with Python and Flask.

## Overview

This project provides a comprehensive backend solution for an insurance management system, allowing for policy retrieval, filtering, sorting. The API is designed to work with a frontend application, supporting features like policy search, premium filtering, and policy type categorization.

## Features

- **Policy Management**: Create, retrieve, update, and delete insurance policies
- **Advanced Filtering**: Filter policies by premium range, policy type, and search terms
- **API Documentation**: Comprehensive documentation with Swagger/OpenAPI

## API Endpoints

### Policies

- `GET /api/policies`: Get all policies with optional filtering and sorting
  - Query Parameters:
    - `search`: Search term for policy names (e.g., "Senior")
    - `min_premium`: Minimum premium amount (e.g., 0)
    - `max_premium`: Maximum premium amount (e.g., 10000)
    - `sort_by`: Field to sort by (e.g., "premium")
    - `policy_type`: Filter by policy type (e.g., "all" or specific type ID)
    - `sort_direction`: Sort order ("asc" or "desc")
  
GET Method  - https://insurance-be.onrender.com/api/policies?search=&min_premium=0&max_premium=10000&min_coverage=0&sort_by=premium&policy_type=all&sort_direction=asc
- `GET /api/policies`: Get a new policy



## Technical Stack

- **Python 3.8+**: Core programming language
- **Flask**: Web framework
- **Flask-RESTful**: Extension for building REST APIs
- **Marshmallow**: Object serialization/deserialization
- **Pyton-JSON-Memory**: Database
