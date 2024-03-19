import paho.mqtt.client as mqtt
import json
import random
import time

# Configuração do cliente MQTT
client = mqtt.Client("python_publisher")

# Conexão ao broker MQTT local
client.connect("localhost", 1891)

# Definindo constantes para a área de simulação
LATITUDE_MIN = -90
LATITUDE_MAX = 90
LONGITUDE_MIN = -180
LONGITUDE_MAX = 180
AREA_SIMULACAO_KM2 = 1000  # Área de 1000 km²

# Função para gerar dados aleatórios do sensor
def generate_sensor_data(sensor_id):
    latitude = round(random.uniform(LATITUDE_MIN, LATITUDE_MAX), 2)
    longitude = round(random.uniform(LONGITUDE_MIN, LONGITUDE_MAX), 2)
    leitura = round(random.uniform(0, 1280), 2)
    
    data = {
        "sensor_id": sensor_id,
        "coordenadas": {
            "latitude": latitude,
            "longitude": longitude
        },
        "leitura": leitura
    }
    return data

# Função para publicar dados do sensor no Broker MQTT
def publish_data(client, topic, data):
    client.publish(topic, json.dumps(data))

# Loop principal para simular dados do sensor e publicá-los
try:
    while True:
        for sensor_id in range(1, 11):  # Simular 10 sensores
            sensor_data = generate_sensor_data(sensor_id)
            topic = "dados_sensor"
            publish_data(client, topic, sensor_data)
            print("Dados publicados:", sensor_data)
        time.sleep(1)  # Aguardar 1 segundo entre a publicação dos dados
except KeyboardInterrupt:
    print("Encerrando...")
    client.disconnect()
