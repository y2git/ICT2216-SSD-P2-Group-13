from flask import Flask, render_template
import mysql.connector
import os

app = Flask(__name__)

# MySQL configurations
app.config['MYSQL_HOST'] = os.getenv('MYSQL_HOST', 'mysql')
app.config['MYSQL_USER'] = os.getenv('MYSQL_USER', 'test')
app.config['MYSQL_PASSWORD'] = os.getenv('MYSQL_PASSWORD', 'test')
app.config['MYSQL_DB'] = os.getenv('MYSQL_DB', 'flask_db')

def get_db_connection():
    conn = mysql.connector.connect(
        host=app.config['MYSQL_HOST'],
        user=app.config['MYSQL_USER'],
        password=app.config['MYSQL_PASSWORD'],
        database=app.config['MYSQL_DB']
    )
    return conn


@app.route('/')
def index():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM test;')
        data = cursor.fetchall()
        db_status = 'Connected to MySQL'
        cursor.close()
        conn.close()
    except Exception as e:
        db_status = f'MySQL connection error: {str(e)}'
    
    return render_template('index.html', db_status=db_status, data=data)
    #return render_template('index.html')
