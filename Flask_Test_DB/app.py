# app.py

from flask import Flask, render_template, request, redirect, url_for, session, flash
import pymysql
# from flask_mysqldb import MySQL
import bcrypt

app = Flask(__name__)
pymysql.install_as_MySQLdb()

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = '123@MySQL'
app.config['MYSQL_DATABASE_DB'] = 'foodie_haven'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

# Create a function to establish a connection to the database
def get_db():
    return pymysql.connect(
        host=app.config['MYSQL_HOST'],
        user=app.config['MYSQL_USER'],
        password=app.config['MYSQL_PASSWORD'],
        db=app.config['MYSQL_DB'],
        cursorclass=pymysql.cursors.DictCursor
    )

# Signup route
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Hash the password before storing it in the database
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

        connection = get_db()

        try:
            with connection.cursor() as cursor:
                # Example query to insert user into the database
                cursor.execute('INSERT INTO users (username, password) VALUES (%s, %s)', (username, hashed_password))
                connection.commit()
                flash('Signup successful! You can now log in.')
                return redirect(url_for('login'))
        finally:
            connection.close()

    return render_template('signup.html')

# Login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        connection = get_db()

        try:
            with connection.cursor() as cursor:
                # Example query to fetch user from the database
                cursor.execute('SELECT * FROM users WHERE username = %s', (username,))
                user = cursor.fetchone()

                if user and bcrypt.checkpw(password.encode('utf-8'), user['password'].encode('utf-8')):
                    # Set the user in the session
                    session['user'] = user['username']
                    flash('Login successful!')
                    return redirect(url_for('home'))
                else:
                    flash('Invalid username or password. Please try again.')
        finally:
            connection.close()

    return render_template('login.html')

# Home route
@app.route('/home')
def home():
    if 'user' in session:
        return render_template('home.html', username=session['user'])
    else:
        return redirect(url_for('login'))

# Logout route
@app.route('/logout')
def logout():
    session.pop('user', None)
    flash('You have been logged out.')
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)