# Use an official Python runtime as a parent image
FROM python:3.9-slim-buster

# Set the working directory in the container
WORKDIR /app

# Add the current directory contents into the container at /app
ADD . /app

# Install necessary dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
ENV NAME WorldFrequencyAnalysis

# Run word_frequency.py when the container launches
CMD ["python", "word_frequency.py"]