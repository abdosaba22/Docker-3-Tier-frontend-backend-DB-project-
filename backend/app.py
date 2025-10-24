from flask import Flask, jsonify
import pymysql.cursors
import os

app = Flask(__name__)

@app.route('/get-records', methods=['GET'])
def get_records():
    DB_HOST = os.environ.get('DB_HOST')
    DB_USER = os.environ.get('DB_USER')
    DB_PASSWORD = os.environ.get('DB_PASSWORD')
    DB_NAME = os.environ.get('DB_NAME')
    
    records = []
    
    try:
        connection = pymysql.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            db=DB_NAME,
            cursorclass=pymysql.cursors.Cursor
        )
        
        with connection.cursor() as cursor:
            sql = "SELECT id, name, major FROM students"
            cursor.execute(sql)
            records = cursor.fetchall()
            
        connection.close()

        return jsonify(records=records), 200

    except Exception as e:
        print(f"Database connection error: {e}")
        return jsonify({"error": "Failed to retrieve records from database"}), 500

@app.route('/')
def hello_docker():
    return 'Hello, Docker! Backend is UP.'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

