import paho.mqtt.client as mqtt
import json
import os
import ssl
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve MQTT credentials from environment variables
broker = os.getenv("MQTT_BROKER")
port = int(os.getenv("MQTT_PORT"))
topic = os.getenv("MQTT_TOPIC")
client_id_subscriber = os.getenv("MQTT_CLIENT_ID_SUBSCRIBER")
username = os.getenv("MQTT_USERNAME")
password = os.getenv("MQTT_PASSWORD")

# Callback chamado quando o cliente MQTT recebe uma mensagem
def on_message(client, userdata, message):
    payload = json.loads(message.payload.decode())
    sensor_id = payload["sensor_id"]
    latitude = payload["coordenadas"]["latitude"]
    longitude = payload["coordenadas"]["longitude"]
    leitura = payload["leitura"]
    print(f"Sensor ID: {sensor_id}")
    print(f"Latitude {latitude:.2f}°")
    print(f"Longitude {longitude:.2f}°")
    print(f"Leitura: {leitura:.2f} W/m²\n")

# Configuração do cliente MQTT
client = mqtt.Client(client_id=client_id_subscriber)
client.username_pw_set(username, password)

# Associação da função de callback à recepção de mensagens
client.on_message = on_message

# Configuração do TLS para o cliente MQTT
client.tls_set_context(ssl.create_default_context())

# Conexão ao broker MQTT
client.connect(broker, port)

# Inscrição no tópico para receber os dados do sensor
client.subscribe(topic)

# Loop principal para manter a conexão e receber mensagens
try:
    client.loop_forever()
except KeyboardInterrupt:
    print("Encerrando...")
    client.disconnect()