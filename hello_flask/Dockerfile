# Stage 1: Build stage
FROM python:3.8-slim AS builder
WORKDIR /app
RUN apt-get update && apt-get install -y \
    gcc \
    python3-dev \
    libmariadb-dev \
    pkg-config
COPY . .
RUN pip install flask mysqlclient

# Stage 2: Production stage
FROM python:3.8-slim AS production
WORKDIR /app
COPY --from=builder /app /app
COPY --from=builder /usr/local/lib/python3.8/site-packages /usr/local/lib/python3.8/site-packages
RUN apt-get update && apt-get install -y libmariadb3 && rm -rf /var/lib/apt/lists/*
EXPOSE 5000
CMD ["python", "app.py"]
