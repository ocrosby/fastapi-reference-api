# Stage 1: Build stage
FROM python:3.8-slim AS builder

# Set the working directory
WORKDIR /app

# Copy the entire project directory
COPY . /app

# Install production dependencies
RUN pip install --no-cache-dir .

# Stage 2: Final stage
FROM python:3.8-slim

# Set the working directory
WORKDIR /app

# Copy only the necessary files from the build stage
COPY --from=builder /app /app

# Expose the port FastAPI is running on
EXPOSE 8000

# Command to run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]