# services/weather-service/Dockerfile
FROM python:3.11-slim

WORKDIR /app
COPY weather_service.py .

RUN pip install fastapi uvicorn

CMD ["uvicorn", "weather_service:app", "--host", "0.0.0.0", "--port", "8001"]
