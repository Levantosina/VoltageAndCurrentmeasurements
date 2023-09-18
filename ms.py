import mysql.connector
import serial

# Azure MySQL database configuration
config = {
    'user': 'levantosina',
    'password': 'Qweqweewq1',
    'host': 'currentvoltage.mysql.database.azure.com',
    'database': 'ms',
    'ssl_ca': "C://Users//levan//Desktop//py_test//DigiCertGlobalRootCA.crt.pem"
}

try:
    # Establishing the connection
    connection = mysql.connector.connect(**config)

    if connection.is_connected():
        print("Connected to MySQL in Azure")

        # Create a cursor
        cursor = connection.cursor()

        # Open serial connection to Arduino
        ser = serial.Serial('COM3', 9600)  # Update COMx with your Arduino's serial port

        while True:
            data = ser.readline().decode().strip()
            voltage, current = map(float, data.split(','))

            insert_query = "INSERT INTO sensor_data (voltage, current) VALUES (%s, %s)"
            cursor.execute(insert_query, (voltage, current))
            connection.commit()

except (mysql.connector.Error, serial.SerialException) as e:
    print("Error:", e)

finally:
    if 'connection' in locals():
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("Connection closed")
