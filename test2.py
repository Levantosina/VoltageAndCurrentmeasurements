import serial
import mysql.connector
from mysql.connector import Error

ser=serial.Serial('COM3', 9600)

# Azure MySQL database configuration
db_config = {
    'user': 'levantosina',
    'password': 'Qweqweewq1',
    'host': 'currentvoltage.mysql.database.azure.com',
    'database': 'ms',
    'ssl_ca': 'C://Users//levan//Desktop//py_test//DigiCertGlobalRootCA.crt.pem'
}

def insert_data(cursor, voltage, current):
    query = "INSERT INTO sensor_data (voltage, current) VALUES (%s, %s)"
    values = (voltage, current)
    cursor.execute(query, values)
    
   

def main():
    try:
        connection = mysql.connector.connect(**db_config)
        if connection.is_connected():
            cursor = connection.cursor()
            print("Connected to Azure MySQL")
            
            while True:
                arduino_data = ser.readline().decode().strip()
                voltage, current = arduino_data.split(',')
                
                insert_data(cursor, voltage, current)
                connection.commit()
                print(f"Data inserted - Voltage: {voltage}, Current: {current}")
                
    except Error as e:
        print("Error",e)
    finally:
        if 'connection' in locals() and connection.is_connected():
            connection.close()
            connection.close()
            print("MySQL connection is closed")
if __name__ == '__main__':
    main()       