import paho.mqtt.client as mqtt
from time import sleep
import random
import ssl
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Read environment variable settings
mqtt_broker = os.getenv("MQTT_BROKER")
mqtt_port = int(os.getenv("MQTT_PORT", 8883))
mqtt_username = os.getenv("MQTT_USERNAME")
mqtt_password = os.getenv("MQTT_PASSWORD")

# Define constants for simulation area
LATITUDE_MIN = -90
LATITUDE_MAX = 90
LONGITUDE_MIN = -180
LONGITUDE_MAX = 180
AREA_SIMULATION_KM2 = 1000  # 1000 km² area

# Client configuration
mqtt_client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, "")

# TLS and authentication settings
mqtt_client.tls_set(cert_reqs=ssl.CERT_REQUIRED, tls_version=ssl.PROTOCOL_TLS)
mqtt_client.username_pw_set(mqtt_username, mqtt_password)

# Connect to the HiveMQ broker
mqtt_client.connect(mqtt_broker, mqtt_port, 60)


def generate_sps30_data():
    # Generate simulated values for mass concentrations
    pm1 = random.uniform(0, 50)  # PM1.0
    pm2_5 = random.uniform(5, 75)  # PM2.5
    pm4 = random.uniform(5, 100)  # PM4.0
    pm10 = random.uniform(10, 120)  # PM10

    # Generate simulated values for number concentrations
    pm0_5_num = random.uniform(0, 1000)  # PM0.5
    pm1_num = random.uniform(100, 5000)  # PM1.0
    pm2_5_num = random.uniform(200, 7000)  # PM2.5
    pm4_num = random.uniform(300, 10000)  # PM4.0
    pm10_num = random.uniform(400, 15000)  # PM10

    # Create message with simulated data including latitude and longitude
    latitude = round(random.uniform(LATITUDE_MIN, LATITUDE_MAX), 2)
    longitude = round(random.uniform(LONGITUDE_MIN, LONGITUDE_MAX), 2)
    message = (f"SPS30 PM1.0: {pm1:.2f} µg/m³, PM2.5: {pm2_5:.2f} µg/m³, "
               f"PM4.0: {pm4:.2f} µg/m³, PM10: {pm10:.2f} µg/m³, "
               f"PM0.5#: {pm0_5_num:.0f} #/cm³, PM1.0#: {pm1_num:.0f} #/cm³, "
               f"PM2.5#: {pm2_5_num:.0f} #/cm³, PM4.0#: {pm4_num:.0f} #/cm³, "
               f"PM10#: {pm10_num:.0f} #/cm³, "
               f"Latitude: {latitude}, Longitude: {longitude}")

    return message


try:
    while True:
        message = generate_sps30_data()
        mqtt_client.publish("sps30/topic", message)
        print(f"Published: {message}")
        sleep(5)  # 5-second interval between publications

except KeyboardInterrupt:
    print("Publication stopped by the user")
    mqtt_client.disconnect()
