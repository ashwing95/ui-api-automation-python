# Use official lightweight Python image
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy requirements.txt (dependencies)
COPY requirements.txt /app/requirements.txt

# Install dependencies
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copy all project files into /app
COPY . /app

# Expose Flask port
EXPOSE 5000

# Command to run your Flask server
CMD ["python", "mock_server/flaskapp.py"]
