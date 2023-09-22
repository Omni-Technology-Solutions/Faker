# Use an official Python runtime as a parent image
FROM python:3.8-slim-buster

# Install any required packages specified in requirements.txt
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copy the current directory contents into the container at /app/
COPY . /app/

# Run your code when the container launches
CMD ["python", "/app/fake_data_toolkit.py"]