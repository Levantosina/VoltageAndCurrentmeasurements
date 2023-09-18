from flask import Flask, request, jsonify
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

# Azure MySQL database configuration
db_config = {
    'user': 'levantosina',
    'password': 'Qweqweewq1',
    'host': 'currentvoltage.mysql.database.azure.com',
    'database': 'ms',
    'ssl_ca': 'C://Users//levan//Desktop//py_test//DigiCertGlobalRootCA.crt.pem'
}

def insert_data(voltage, current):
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()
        query = "INSERT INTO sensor_data (voltage, current) VALUES (%s, %s)"
        values = (voltage, current)
        cursor.execute(query, values)
        connection.commit()
        cursor.close()
        connection.close()
        return True
    except Error as e:
        print("Error", e)
        return False

@app.route('/api/data', methods=['POST'])
def receive_data():
    data = request.json
    voltage = data.get('voltage')
    current = data.get('current')
    
    if voltage is not None and current is not None:
        if insert_data(voltage, current):
            return jsonify({"message": "Data inserted successfully"})
        else:
            return jsonify({"message": "Error inserting data"}), 500
    else:
        return jsonify({"message": "Invalid data format"}), 400

if __name__ == '__main__':
    app.run(debug=True)