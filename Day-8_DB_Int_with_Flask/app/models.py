from flask import Flask
# from flask_mysql import MySQL
from flaskext.mysql import MySQL

app = Flask(__name__)
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = '123@MySQL'
app.config['MYSQL_DATABASE_DB'] = 'foodie_haven'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

mysql = MySQL(app)

cursor = mysql.connection.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS menu_items (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        description TEXT,
        price DECIMAL(10, 2) NOT NULL,
        availability BOOLEAN NOT NULL
    )
''')

mysql.connection.commit()
cursor.close()
