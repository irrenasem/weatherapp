# Use an official Python runtime as a parent image
FROM python:3.9-alpine

# Set the working directory
WORKDIR /app

# Copy only the necessary files
COPY requirements.txt .
COPY weather_app.py .

# Install any dependencies
RUN pip install -r requirements.txt

# Run your application
CMD ["python", "weather_app.py"]
