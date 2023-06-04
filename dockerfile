# Use an official Python runtime as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the Python script to the container
COPY . /app

# Install any necessary dependencies
RUN pip install pytest

# Set the command to run the application
CMD ["python", "password_generator.py"]
