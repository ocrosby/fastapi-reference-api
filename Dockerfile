FROM python:3.8-slim

# Set the working directory
WORKDIR /app

# Copy the entire project directory
COPY . /app

# Install production dependencies
RUN pip install --no-cache-dir .

# Install uvicorn
RUN pip install uvicorn[standard]

# Expose the port FastAPI is running on
EXPOSE 8000

# Command to run the application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
