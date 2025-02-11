# Use the official Python image from the Docker Hub
FROM python:3.10-slim AS builder

# Set the working directory
WORKDIR /src

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PIPENV_VENV_IN_PROJECT=1

# Install pipenv
RUN pip install --upgrade pip && pip install pipenv==2024.4.1

# Copy the Pipfile and Pipfile.lock
COPY Pipfile Pipfile.lock /src/

# Install dependencies
RUN pipenv install --system --deploy

# Ensure the installed binary is on the `PATH`
ENV PATH="/src/.venv/bin:$PATH"

FROM builder AS release
# Set the working directory
WORKDIR /app

# Copy the rest of the application code
COPY . /app/

# No CMD instruction, as it will be managed by docker-compose
