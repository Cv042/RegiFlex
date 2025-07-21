"""
Flask Authentication App with MySQL Database
Main application file with routes for registration, login, and welcome pages
"""
from flask import Flask, render_template, request, redirect, url_for, flash, session
from config import Config
from models import db, User
import traceback

# Initialize Flask app
app = Flask(__name__)
app.config.from_object(Config)

# Initialize database with app
db.init_app(app)

@app.route('/')
def index():
    """
    Home page - redirect to login if not logged in, otherwise to welcome
    """
    if 'user_id' in session:
        return redirect(url_for('welcome'))
    return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    """
    User registration page
    GET: Display registration form
    POST: Process registration form
    """
    if request.method == 'POST':
        username = request.form['username'].strip()
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        
        # Validation
        if not username or not password:
            flash('Username and password are required!', 'error')
            return render_template('register.html')
        
        if len(username) < 3:
            flash('Username must be at least 3 characters long!', 'error')
            return render_template('register.html')
        
        if len(password) < 6:
            flash('Password must be at least 6 characters long!', 'error')
            return render_template('register.html')
        
        if password != confirm_password:
            flash('Passwords do not match!', 'error')
            return render_template('register.html')
        
        # Check if user already exists
        if User.get_by_username(username):
            flash('Username already exists! Please choose a different one.', 'error')
            return render_template('register.html')
        
        try:
            # Create new user
            user = User.create_user(username, password)
            flash('Registration successful! You can now log in.', 'success')
            return redirect(url_for('login'))
        
        except Exception as e:
            # Log the error for debugging
            print(f"Registration error: {str(e)}")
            print(traceback.format_exc())
            db.session.rollback()
            flash('Registration failed. Please try again.', 'error')
            return render_template('register.html')
    
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    """
    User login page
    GET: Display login form
    POST: Process login form
    """
    if request.method == 'POST':
        username = request.form['username'].strip()
        password = request.form['password']
        
        # Validation
        if not username or not password:
            flash('Username and password are required!', 'error')
            return render_template('login.html')
        
        # Find user and check password
        user = User.get_by_username(username)
        if user and user.check_password(password):
            # Login successful
            session['user_id'] = user.id
            session['username'] = user.username
            flash(f'Welcome back, {user.username}!', 'success')
            return redirect(url_for('welcome'))
        else:
            # Login failed
            flash('Invalid username or password!', 'error')
            return render_template('login.html')
    
    return render_template('login.html')

@app.route('/welcome')
def welcome():
    """
    Welcome page - only accessible to logged-in users
    """
    if 'user_id' not in session:
        flash('Please log in to access this page.', 'error')
        return redirect(url_for('login'))
    
    return render_template('welcome.html', username=session.get('username'))

@app.route('/logout')
def logout():
    """
    Logout route - clears session and redirects to login
    """
    session.clear()
    flash('You have been logged out successfully.', 'info')
    return redirect(url_for('login'))

@app.errorhandler(404)
def not_found(error):
    """
    Handle 404 errors
    """
    return render_template('login.html'), 404

@app.errorhandler(500)
def internal_error(error):
    """
    Handle 500 errors
    """
    db.session.rollback()
    flash('An internal error occurred. Please try again.', 'error')
    return render_template('login.html'), 500

def create_tables():
    """
    Create database tables
    """
    with app.app_context():
        try:
            db.create_all()
            print("Database tables created successfully!")
        except Exception as e:
            print(f"Error creating tables: {str(e)}")
            print(traceback.format_exc())

if __name__ == '__main__':
    # Create tables on startup
    create_tables()
    
    # Run the app
    print("Starting Flask app...")
    print("Visit http://127.0.0.1:5000 in your browser")
    app.run(debug=True, port=5000)