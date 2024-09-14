# Use an official Python runtime as a base image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy current directory contents into the container at /app
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port the app runs on
# EXPOSE 5001

# # Set environment variables
# ENV FLASK_APP=app
# ENV FLASK_ENV=development
# ENV FLASK_RUN_PORT=5001
# ENV FLASK_RUN_HOST=0.0.0.0

# Run the Flask app
CMD ["flask", "run"]
