# Use an official Python runtime as a parent image
FROM python:3.10-slim  

# Install dependencies
RUN apt-get update && apt-get install -y \
    pymol \
    tk \
    && apt-get clean

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install Python dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expose port 80
EXPOSE 80

# Run the application
CMD ["python", "main.py"]

