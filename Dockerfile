# Stage 1: Builder stage to install dependencies
FROM python:3.11-slim as builder

WORKDIR /usr/src/app

# Create and activate a virtual environment
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Stage 2: Final production image
FROM python:3.11-slim

# Create a non-root user
RUN addgroup --system app && adduser --system --group app

WORKDIR /home/app

# Copy virtual environment from builder stage
COPY --from=builder /opt/venv /opt/venv

# Copy application code
COPY app.py .

# Change ownership to non-root user
RUN chown -R app:app /home/app

# Set environment variables
ENV PATH="/opt/venv/bin:$PATH"
ENV PYTHON_ENV=production
ENV PORT=5000

# Switch to non-root user
USER app

EXPOSE 5000

# Run the application with Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
