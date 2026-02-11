# Use Python 3.11 slim image as base
FROM python:3.11-slim

# Install system dependencies for Tkinter and GUI support
RUN apt-get update && apt-get install -y \
    python3-tk \
    tk \
    libx11-6 \
    libxext6 \
    libxrender1 \
    libxft2 \
    libxss1 \
    xdg-utils \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application files
COPY The_card.py .
COPY Resources/ ./Resources/

# Set environment variables for display
ENV DISPLAY=:0

# Run the application
CMD ["python", "The_card.py"]
