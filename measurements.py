import serial
import mysql.connector
from mysql.connector import Error
from flask import Flask, request, jsonify

app = Flask(__name__)

# Serial communication setup
ser = serial.Serial('COM3', 9600)  # Adjust the port and baud rate as needed

# Azure database configuration
db_config = {
    'user': 'levantosina',
    'password': 'Qweqweewq1',
    'host': 'currentvoltage.mysql.database.azure.com',
    'database': 'ms',
    'ssl_ca': 'C://Users//levan//Desktop//py_test//DigiCertGlobalRootCA.crt.pem'
}

# Function to insert data into the database
def insert_data(cursor, voltage, current):
    query = "INSERT INTO sensor_data (voltage, current) VALUES (%s, %s)"
    values = (voltage, current)
    cursor.execute(query, values)

# Define an API route
@app.route('/insert_data', methods=['POST'])
def api_insert_data():
    try:
        connection = mysql.connector.connect(**db_config)
        if connection.is_connected():
            cursor = connection.cursor()
            print("Connected to the Azure database")

            data = request.json  # Assuming the request contains JSON with "voltage" and "current" keys
            voltage = data.get('voltage')
            current = data.get('current')

            insert_data(cursor, voltage, current)
            connection.commit()
            print(f"Data inserted - Voltage: {voltage}, Current: {current}")

            return jsonify({"message": "Data inserted successfully"})
        
    except Error as e:
        return jsonify({"error": str(e)})
    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
            print("Connection to the database closed")
if __name__ == "__main__":
    app.run(debug=True) 
