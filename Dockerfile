# Use an official Python runtime as a base image
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the Python script into the container
COPY main.py .
RUN pip install fastapi uvicorn

EXPOSE 8000


# Set the default command to run your script
CMD ["python", "main.py"]