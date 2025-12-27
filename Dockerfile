# Stage 1: Builder
FROM python:3.11-slim-bookworm AS builder

WORKDIR /opt/app

# Create and activate a virtual environment
ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Stage 2: Final Image
FROM python:3.11-slim-bookworm AS final

# Create a non-root user
RUN groupadd --system nonroot && \
    useradd --system --gid nonroot --shell /bin/bash nonroot

WORKDIR /home/nonroot/app

# Copy virtual environment from builder stage
COPY --from=builder /opt/venv /opt/venv

# Copy application code
COPY app.py .

# Set ownership and permissions
RUN chown -R nonroot:nonroot /home/nonroot/app
USER nonroot

# Activate the virtual environment
ENV PATH="/opt/venv/bin:$PATH"

EXPOSE 5000

# Set the command to run the application using Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "2", "app:app"]
