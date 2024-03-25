import paho.mqtt.client as mqtt
import json
import random
import time

# Configuração do cliente MQTT para publicação
client_id_publisher = "python_publisher"
publisher_client = mqtt.Client(client_id=client_id_publisher, protocol=mqtt.MQTTv311, callback_api_version=mqtt.CallbackAPIVersion.VERSION2)

# Configuração do cliente MQTT para subscrição
client_id_subscriber = "python_subscriber"
subscriber_client = mqtt.Client(client_id=client_id_subscriber, protocol=mqtt.MQTTv311, callback_api_version=mqtt.CallbackAPIVersion.VERSION2)

# Conexão ao broker MQTT local para publicação
publisher_client.connect("localhost", 1891)

# Conexão ao broker MQTT local para subscrição
subscriber_client.connect("localhost", 1891)

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

# Contador de amostras enviadas
samples_sent = 0
total_samples = 30  # Número total de amostras desejadas

# Loop principal para simular dados do sensor e publicá-los
try:
    while samples_sent < total_samples:
        for sensor_id in range(1, 11):  # Simular 10 sensores
            sensor_data = generate_sensor_data(sensor_id)
            topic = "dados_sensor"
            publish_data(publisher_client, topic, sensor_data)
            print("Dados publicados:", sensor_data)
            samples_sent += 1  # Incrementa o contador de amostras enviadas
            if samples_sent >= total_samples:
                break  # Sai do loop se o número total de amostras foi atingido
        time.sleep(1)  # Aguardar 1 segundo entre a publicação dos dados
except KeyboardInterrupt:
    print("Encerrando...")
    publisher_client.disconnect()
    subscriber_client.disconnect()