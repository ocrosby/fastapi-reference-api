# Use the official Python image from the Docker Hub
FROM python:3.8-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY pyproject.toml /app

# Install dependencies
RUN pip install --no-cache-dir -e .[dev]

# Copy the FastAPI application
COPY . /app

# Expose the port FastAPI is running on
EXPOSE 8000

# Command to run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]