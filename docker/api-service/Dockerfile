FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Create static directory
RUN mkdir -p static

COPY main.py .
COPY startup.sh .
RUN chmod +x startup.sh

# Copy web frontend HTML to static directory
COPY ../web-frontend/index.html ./static/

EXPOSE 8000

CMD ["./startup.sh"]