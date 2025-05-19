# Use official Python image
FROM python:3.10-slim

# Working directory
WORKDIR /app

# Copy requirements
COPY requirements.txt ./

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY app.py ./

# Expose port
EXPOSE 7860

# Launch the app
CMD ["python", "app.py"] 