# Accept build arguments for the API keys
ARG OPENAI_API_KEY
ARG SERPA_API

# Set them as environment variables
ENV OPENAI_API_KEY=$OPENAI_API_KEY
ENV SERPA_API=$SERPA_API

# Use an official Python runtime as a parent image
FROM python:3.11-slim-buster

# Set the working directory in the container to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 8080

# Define environment variable (if needed)
# ENV NAME World

# Run your application
CMD ["python3", "main.py"]
