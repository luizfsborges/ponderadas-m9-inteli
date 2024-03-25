import paho.mqtt.client as mqtt
import json

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
client = mqtt.Client("python_subscriber")

# Associação da função de callback à recepção de mensagens
client.on_message = on_message

# Conexão ao broker MQTT local
client.connect("localhost", 1891)

# Inscrição no tópico para receber os dados do sensor
client.subscribe("dados_sensor")

# Loop principal para manter a conexão e receber mensagens
try:
    client.loop_forever()
except KeyboardInterrupt:
    print("Encerrando...")
    client.disconnect()
