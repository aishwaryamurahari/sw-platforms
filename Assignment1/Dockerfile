# Use an official Python runtime as a base image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy current directory contents into the container at /app
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# RUN apt-get update && apt-get install -y vim

# CMD ["sh", "-c", "python init_db.py && flask run && pyrun test_blog.py"]
# # Run the Flask app
CMD ["flask", "run"]
