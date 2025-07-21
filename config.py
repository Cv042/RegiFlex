"""
Configuration file for Flask application
Contains database connection settings and secret key
"""
import os

class Config:
    # Secret key for session management and CSRF protection
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your-secret-key-change-this-in-production'
    
    # MySQL database configuration
    # Format: mysql+pymysql://username:password@host:port/database_name
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'mysql+pymysql://flask_app_user:flask_password@localhost:3306/flask_auth_db'
    
    # Disable SQLAlchemy event system to save resources
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Optional: Enable SQL query logging for debugging
    # SQLALCHEMY_ECHO = True