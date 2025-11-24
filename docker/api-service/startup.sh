#!/bin/bash

# Wait for database to be ready
echo "Waiting for database to be ready..."
while ! nc -z $DB_HOST $DB_PORT; do
  sleep 1
done

echo "Database is ready! Starting API server..."

# Start the FastAPI application
exec uvicorn main:app --host 0.0.0.0 --port 8000