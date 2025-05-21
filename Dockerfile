FROM python:3.12-slim-bullseye AS builder

WORKDIR /app
COPY requirements.txt .

RUN apt-get update && apt-get install -y \
    gcc \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir -r requirements.txt

FROM python:3.12-slim-bullseye

WORKDIR /app

RUN apt-get update && apt-get install -y \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

COPY --from=builder /usr/local/lib/python3.12/site-packages/ /usr/local/lib/python3.12/site-packages/
COPY --from=builder /usr/local/bin/ /usr/local/bin/
COPY . .

RUN useradd -m appuser && chown -R appuser:appuser /app
RUN chmod +x start.sh
USER appuser

EXPOSE 9667
CMD ["./start.sh"]
