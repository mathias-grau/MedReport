# Use the official Python 3.12 slim image as a base image
FROM python:3.12-slim

# Prevent Python from writing pyc files to disk and enable unbuffered logging
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory for dependency installation
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt

# Create a non-root user with UID 1000
RUN useradd -m -u 1000 user

# Set environment variables for the non-root user
ENV HOME=/home/user
ENV PATH=$HOME/.local/bin:$PATH

# Switch to non-root user
USER user

ENV HOME=/home/user \
	PATH=/home/user/.local/bin:$PATH


# Create the MedReport directory inside the container
RUN mkdir -p $HOME/app/MedReport

# Copy the project into the MedReport folder
COPY --chown=user . $HOME/app/MedReport

# Set working directory in the container for the application
WORKDIR $HOME/app/MedReport

# (Optional) Create a directory for caching downloaded models (e.g., for Hugging Face)
RUN mkdir -p $HOME/.cache/huggingface

# Set Flask environment variables to ensure it runs on the correct host and port
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=7860

# Expose the port that your app will run on
EXPOSE 7860

# Start the Flask application
CMD ["flask", "run"]
