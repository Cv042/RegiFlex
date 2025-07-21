"""
Database models for the Flask authentication system
Defines the User model with password hashing functionality
"""
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

# Initialize SQLAlchemy instance
db = SQLAlchemy()

class User(db.Model):
    """
    User model for storing user credentials
    """
    # Table name in MySQL
    __tablename__ = 'users'
    
    # Primary key
    id = db.Column(db.Integer, primary_key=True)
    
    # Username - unique and required
    username = db.Column(db.String(80), unique=True, nullable=False, index=True)
    
    # Password hash - store hashed password, never plain text
    password_hash = db.Column(db.String(255), nullable=False)
    
    # Optional: timestamp for when user registered
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __init__(self, username, password):
        """
        Initialize user with username and password
        Password is automatically hashed
        """
        self.username = username
        self.set_password(password)
    
    def set_password(self, password):
        """
        Hash and set the user's password
        """
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        """
        Check if provided password matches the stored hash
        Returns True if password is correct, False otherwise
        """
        return check_password_hash(self.password_hash, password)
    
    def __repr__(self):
        """
        String representation of User object
        """
        return f'<User {self.username}>'
    
    @classmethod
    def get_by_username(cls, username):
        """
        Find user by username
        Returns User object or None if not found
        """
        return cls.query.filter_by(username=username).first()
    
    @classmethod
    def create_user(cls, username, password):
        """
        Create a new user with the given username and password
        Returns the new User object
        """
        user = cls(username=username, password=password)
        db.session.add(user)
        db.session.commit()
        return user