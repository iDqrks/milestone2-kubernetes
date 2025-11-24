from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import mysql.connector
import os
import socket
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="Brent Verlinden API", version="1.0.0")

# CORS middleware - CRITICAL voor browser toegang
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Sta alle origins toe voor development
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Database configuration
DB_CONFIG = {
    'host': os.getenv('DB_HOST', 'bv-mariadb'),
    'user': os.getenv('DB_USER', 'brent_user'),
    'password': os.getenv('DB_PASSWORD', 'brent_password'),
    'database': os.getenv('DB_NAME', 'brent_db'),
    'port': os.getenv('DB_PORT', '3306')
}

def get_db_connection():
    try:
        connection = mysql.connector.connect(**DB_CONFIG)
        logger.info("✅ Database connected")
        return connection
    except mysql.connector.Error as e:
        logger.error(f"❌ Database connection failed: {e}")
        return None

@app.get("/")
async def root():
    return {"message": "Brent Verlinden API Service", "status": "running"}

@app.get("/health")
async def health_check():
    db_status = "connected" if get_db_connection() else "disconnected"
    return {
        "status": "healthy",
        "database": db_status,
        "container_id": socket.gethostname()
    }

@app.get("/user")
async def get_user():
    connection = get_db_connection()
    if not connection:
        return {"name": "Brent Verlinden"}
    
    try:
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT name FROM users WHERE id = 1")
        result = cursor.fetchone()
        cursor.close()
        connection.close()
        
        if result:
            return {"name": result['name']}
        else:
            return {"name": "Brent Verlinden"}
    except Exception as e:
        logger.error(f"Error fetching user: {e}")
        return {"name": "Brent Verlinden"}

@app.get("/container")
async def get_container_info():
    return {
        "container_id": socket.gethostname(),
        "service": "brent-api",
        "status": "running"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)