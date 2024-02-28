# Use the official Python base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the code files into the container
COPY . .

# Install the required packages
RUN pip install Flask mysql-connector-python

# Expose the required ports
EXPOSE 5000

# Start the Flask app
CMD ["python", "app.py"]
