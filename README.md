# 🔐 Flask Authentication App

A simple and secure user authentication system built using **Flask** and **MySQL**. The application includes registration, login, logout, and session management with proper validation and security practices.

---

## 📁 Project Structure

flask-auth-app/
├── app.py # Main Flask application
├── config.py # Configuration settings
├── models.py # Database models
├── requirements.txt # Python dependencies
└── templates/
├── base.html # Base layout with Bootstrap
├── register.html # User registration form
├── login.html # Login form
└── welcome.html # Welcome dashboard

yaml
Copy
Edit

---

## 🔧 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/flask-auth-app.git
cd flask-auth-app
2. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
3. Configure MySQL Database
Edit config.py with your MySQL credentials:

python
Copy
Edit
MYSQL_USER = 'your_mysql_username'
MYSQL_PASSWORD = 'your_mysql_password'
MYSQL_HOST = 'localhost'
MYSQL_PORT = '3306'
MYSQL_DATABASE = 'flask_auth_db'
4. Create the Database
Login to MySQL and run:

sql
Copy
Edit
CREATE DATABASE flask_auth_db;
▶️ Run the Application
bash
Copy
Edit
python app.py
Visit: http://127.0.0.1:5000

✅ Features Implemented
🔐 Authentication
User Registration

Login with sessions

Logout functionality

Password hashing via werkzeug.security

💬 Flash Messaging
Duplicate user detection

Login failures

Successful registration/logout alerts

🛡️ Security
Secure password storage

CSRF protection (via Flask secret key)

Input validation (client + server)

💡 UI/UX
Responsive UI with Bootstrap 5

Flash messages with auto-dismiss

Navigation bar with login/logout status

🧪 Usage
Route	Description
/register	Register a new user
/login	Login with credentials
/welcome	Protected dashboard (after login)
/logout	Logout and destroy session

🛠️ Requirements
Python 3.8+

Flask

Flask-MySQL or PyMySQL

MySQL Server

Install all dependencies via:

bash
Copy
Edit
pip install -r requirements.txt
📸 Screenshots (Optional)
You can add UI screenshots here to showcase your registration/login/welcome pages.

📃 License
This project is licensed under the MIT License - feel free to use and modify.

🙌 Contributions
Pull requests are welcome. If you'd like to add more features like:

Forgot password

User roles

Admin dashboard

Feel free to fork and build!

