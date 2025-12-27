# Stage 1: Builder - Install dependencies in a virtual environment
FROM python:3.11-slim as builder

WORKDIR /opt/app

# Create and activate a virtual environment
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Stage 2: Final - Create the final lightweight image
FROM python:3.11-slim

WORKDIR /app

# Copy virtual environment and application code from builder stage
COPY --from=builder /opt/venv /opt/venv
COPY app.py .

# Activate the virtual environment
ENV PATH="/opt/venv/bin:$PATH"

# Create a non-root user for security
RUN addgroup --system --gid 1001 nonroot && \
    adduser --system --uid 1001 --ingroup nonroot nobody
USER nobody

# Expose application port
EXPOSE 5000

# Run the application with Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "2", "--threads", "4", "app:app"]
