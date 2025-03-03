# Use a lightweight Python image
FROM python:3.9

# Set the working directory
WORKDIR /app

# Copy everything from your repo into the container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the Flask default port
EXPOSE 7860

# Run the Flask app
CMD ["python", "app.py"]
