# fitness-tracker-api

A simple RESTful API built with Flask and PostgreSQL to track users' health metrics like steps, heart rate, calories burned, weight, and more. The API includes user authentication using JWT.

## Features

- User registration and login with hashed passwords
- JWT-based authentication
- Log and store health metrics
- Retrieve metrics securely per user
- Containerized using Docker & PostgreSQL
- PGAdmin integration for database management

## 📂 Project Structure

```
fitness-tracker-api/
├── app.py                     # Entry point for Flask app
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .env
├── models/
│   └── health_metrics.py      # SQLAlchemy models
├── routes/
│   ├── health.py              # Routes for logging metrics
│   └── auth.py                # Routes for registering users
│   └── login.py               # Routes for user login
├── utils/
│   ├── security.py            # Password hashing & verification
│   └── jwt_handler.py         # JWT generation and decoding
├── database/
│   └── connection.py          # DB engine and session setup
├── frontend/
├── index.html
├── assets
│   └── css
│   └── js
│   └── img

```

## Tech Stack

- **Backend:** Python, Flask
- **Database:** PostgreSQL
- **ORM:** SQLAlchemy
- **Authentication:** JWT
- **Containerization:** Docker
- **Database Admin:** PGAdmin

## Getting Started

### Prerequisites

- Docker
- Docker Compose

### Running the app

```bash
docker-compose up --build
```

- API: [http://localhost:5000](http://localhost:5000)
- PGAdmin: [http://localhost:8080](http://localhost:8080)

### Sample Endpoints

- `POST /api/create-test-user` – Register a new user
- `POST /login` – Login and get a JWT token
- `POST /metrics` – Log user metrics (auth required)

## Authentication

- Secure endpoints with JWT.
- Include token in `Authorization` header:  

## TODO

- Add unit tests
- Expand metric tracking
- Frontend UI for user dashboard

---

![arch diagram](https://github.com/Ibraheem101/fitness-tracker-api/blob/main/images/fitness%20tracker.jpg)

---
### Screenshots
<img src="https://github.com/Ibraheem101/fitness-tracker-api/blob/main/images/register.png" alt="screenshot" height="250" width="150">