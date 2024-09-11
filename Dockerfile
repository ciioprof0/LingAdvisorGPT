# Use the official Python image.
FROM python:3.12-slim

# Set the working directory in the container.
WORKDIR /project-root

# Copy the requirements.txt first to leverage Docker cache.
COPY requirements.txt .

# Install the dependencies.
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code.
COPY . .

# Set environment variables for Flask.
ENV FLASK_APP=src.entrypoints.api.app
ENV FLASK_ENV=development

# Expose the port on which the app will run.
EXPOSE 5000

# Run the application.
CMD ["flask", "run", "--host=0.0.0.0"]
