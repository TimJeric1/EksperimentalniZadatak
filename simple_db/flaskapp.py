from flask import Flask, jsonify
import mysql.connector.pooling
import time

app = Flask(__name__)

# Initialize connection pool configurations
dbconfig = {
    "host": "localhost",
    "user": "root",
    "password": "root",
    "database": "test_db"
}

# Create a connection pool
pool = mysql.connector.pooling.MySQLConnectionPool(pool_name="my_pool", pool_size=5, **dbconfig)

# Function to get a connection from the pool with retry
def get_connection_from_pool():
    while True:
        try:
            return pool.get_connection()
        except mysql.connector.Error as e:
            print(f"Failed getting connection. Retrying in 1 second... Error: {e}")
            time.sleep(1)

# Route that performs a database read operation
@app.route('/read-users')
def read_users():
    try:
        # Attempt to get a connection from the pool with retries
        cnx = get_connection_from_pool()

        cursor = cnx.cursor()
        
        # Execute your read query (replace 'your_table' and 'your_column' with appropriate names)
        query = 'SELECT * FROM users'
        cursor.execute(query)
        
        # PROCESSING
        time.sleep(0.5)

        data = cursor.fetchall()
        
        cursor.close()
        cnx.close()

        # Convert data to JSON format and return
        return jsonify(data)

    except mysql.connector.Error as err:
        return f"Error: {err}\n"

if __name__ == '__main__':
    app.run(debug=True)
