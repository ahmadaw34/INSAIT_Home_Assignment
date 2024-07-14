# INSAIT-Assignment(Backend Developer)

## Overview
This project is a simple Flask server that exposes an endpoint to ask a question. The server sends the question to an OpenAI API, receives the answer, and saves both the question and the answer in a PostgreSQL database. The server and the database are dockerized and run with Docker Compose. The project includes a pytest test to ensure the endpoint works as expected.

## Features
- Flask server with an endpoint to handle questions
- Integration with OpenAI API to get answers for questions
- PostgreSQL database to store questions and answers
- Database migrations managed by Alembic
- Dockerized Flask server and PostgreSQL database
- Docker Compose to manage and run containers
- Test implemented using pytest

## Requirements
- Docker and Docker Compose
- OpenAI API key (free tier can be used)
- Python 3.9

## Installation And Running Instructions:


1. **Clone the Repository:**
```shell
git clone https://github.com/ahmadaw34/INSAIT_Home_Assignment.git
cd INSAIT_Home_Assignment
```

2. **Build Docker Images After turning the Docker ON:**
```shell
docker-compose build
```

3. **Run the Test:**
```shell
docker-compose up
```
