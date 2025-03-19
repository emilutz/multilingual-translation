# Base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install UV package manager
RUN pip install uv

# Copy dependency files
COPY pyproject.toml .
COPY requirements.txt .
COPY requirements.lock .

# Install from the lock file for deterministic builds
RUN uv pip install --system --no-deps -r requirements.lock

# Copy the rest of the application
COPY . .

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# Command to run when container starts
CMD ["python", "main.py"]
