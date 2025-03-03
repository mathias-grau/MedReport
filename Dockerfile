# Use Python 3.12 as base
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy all files to the container
COPY . .

# Create uploads directory and set permissions
RUN mkdir -p /app/uploads && chmod -R 777 /app/uploads

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port (if needed)
EXPOSE 7860

# Run Flask
CMD ["python", "-m", "app.app"]
