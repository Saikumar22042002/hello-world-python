# Stage 1: Builder
# This stage installs dependencies into a virtual environment.
FROM python:3.11-slim-bookworm as builder

WORKDIR /app

# Create and activate a virtual environment
ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Stage 2: Final Image
# This stage creates the final, minimal image for production.
FROM python:3.11-slim-bookworm

WORKDIR /app

# Copy the virtual environment from the builder stage
COPY --from=builder /opt/venv /opt/venv

# Copy the application source code
COPY app.py .

# Set the path to include the virtual environment's binaries
ENV PATH="/opt/venv/bin:$PATH"

# Expose the port the application will run on
EXPOSE 5000

# Run as a non-root user for security
USER nobody

# Command to run the application using Gunicorn
# Gunicorn is a production-grade WSGI server.
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "4", "app:app"]
