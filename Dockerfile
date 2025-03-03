# Use the official Python 3.12 slim image as a base image
FROM python:3.12-slim

# Prevent Python from writing pyc files to disk and enable unbuffered logging
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the rest of your project files
COPY . /app/

# Run download_models.py to download the model files
RUN python download_models.py

# Set Flask environment variables to ensure it runs on the correct host and port
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
# Hugging Face Spaces expects your app to listen on port 7860, so we set it here
ENV FLASK_RUN_PORT=7860

# Expose the port that your app will run on
EXPOSE 7860

# Start the Flask application
CMD ["flask", "run"]
