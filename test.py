import serial
import requests
import time

ser = serial.Serial('COM3', 9600)  # Adjust the port and baud rate as needed
api_url = "https://shrouded-savannah-08736-745c66f6276e.herokuapp.com/insert_data"  # Replace with your Azure Web App URL

while True:
    arduino_data = ser.readline().decode().strip()
    voltage, current = arduino_data.split(',')  # Assuming data format: "voltage,current"

    data = {"voltage": voltage, "current": current}

    try:
        response = requests.post(api_url, json=data)
        response.raise_for_status()  # Check for HTTP request errors
        print("Data sent to API successfully")
    except requests.exceptions.RequestException as e:
        print("Error sending data:", e)

    time.sleep(30)  # Delay before sending the next set of data