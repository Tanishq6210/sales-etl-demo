
FROM python:3.11-slim

WORKDIR /app

COPY etl.py .
COPY data/ ./data/

CMD ["python", "etl.py"]
