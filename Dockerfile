# Stage 1: Builder/dependencies
FROM python:3.11-slim as builder

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip wheel --no-cache-dir --wheel-dir /wheels -r requirements.txt

# Stage 2: Final image
FROM python:3.11-slim

WORKDIR /app

# Create a non-privileged user
RUN addgroup --system --gid 1001 appgroup && \
    adduser --system --uid 1001 --ingroup appgroup --no-create-home appuser

COPY --from=builder /wheels /wheels
COPY requirements.txt .
RUN pip install --no-cache /wheels/*

COPY app.py .

# Switch to the non-privileged user
USER appuser

EXPOSE 5000

# Use gunicorn for production
CMD ["gunicorn", "--workers", "2", "--bind", "0.0.0.0:5000", "app:app"]