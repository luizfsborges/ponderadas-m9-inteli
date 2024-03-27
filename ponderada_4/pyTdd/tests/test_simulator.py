import unittest
import paho.mqtt.client as mqtt
import time
import ssl
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Configuração dos parâmetros MQTT
broker = os.getenv("MQTT_BROKER")
port = int(os.getenv("MQTT_PORT"))
topic = os.getenv("MQTT_TOPIC")
client_id_publisher = os.getenv("MQTT_CLIENT_ID_PUBLISHER")
client_id_subscriber = os.getenv("MQTT_CLIENT_ID_SUBSCRIBER")
username = os.getenv("MQTT_USERNAME")
password = os.getenv("MQTT_PASSWORD")

# Variável global para armazenar mensagens recebidas para validação
received_messages = []

def tls_set(client):
    """Configura a conexão TLS."""
    client.tls_set(cert_reqs=ssl.CERT_REQUIRED, tls_version=ssl.PROTOCOL_TLS)
    client.username_pw_set(username, password)

class TestIoTSimulator(unittest.TestCase):
    def setUp(self):
        # Configuração do cliente para publicação
        self.publisher_client = mqtt.Client(client_id=client_id_publisher, clean_session=True)
        tls_set(self.publisher_client)  # Aplica configuração TLS para HiveMQ
        self.publisher_client.connect(broker, port)

        # Configuração do cliente para subscrição
        self.subscriber_client = mqtt.Client(client_id=client_id_subscriber, clean_session=True)
        tls_set(self.subscriber_client)  # Aplica configuração TLS para HiveMQ
        self.subscriber_client.on_message = self.on_message
        self.subscriber_client.connect(broker, port)
        self.subscriber_client.subscribe(topic)
        self.subscriber_client.loop_start()
        time.sleep(1)  # Garante que o subscriber seja configurado antes dos testes

    def tearDown(self):
        # Desconecta os clientes MQTT após os testes
        self.subscriber_client.loop_stop()
        self.subscriber_client.disconnect()
        self.publisher_client.disconnect()

    def on_message(self, client, userdata, message):
        # Função callback para mensagens recebidas
        received_messages.append(message.payload.decode())
        print(f"Received message in test subscriber: {message.payload.decode()}")

    def test_data_reception(self):
        """Testa se os dados são recebidos corretamente pelo broker MQTT."""
        test_message = "Test message"
        self.publisher_client.publish(topic, test_message)
        time.sleep(2)  # Aguarda 2 segundos para a mensagem ser recebida
        self.assertIn(test_message, received_messages, "A mensagem de teste não foi recebida.")

    def test_data_validation(self):
        """Testa se os dados recebidos correspondem aos dados enviados."""
        # Supõe que test_data_reception já adicionou uma mensagem a received_messages
        test_message = "Test message"
        self.assertEqual(received_messages[-1], test_message, "A mensagem recebida não corresponde à mensagem enviada.")

    def test_message_dispatch_rate(self):
        """Testa se as mensagens são enviadas na taxa esperada."""
        start_time = time.time()
        for _ in range(2):
            self.publisher_client.publish(topic, "Rate test message")
            time.sleep(5)  # Aguarda 5 segundos entre cada mensagem

        end_time = time.time()
        duration = end_time - start_time

        # Espera-se 2 mensagens enviadas, com intervalo de 5 segundos entre cada uma
        expected_duration_min = 9  # segundos (2 mensagens * 5 segundos de intervalo - 1 segundo de margem)
        expected_duration_max = 11  # segundos (2 mensagens * 5 segundos de intervalo + 1 segundo de margem)
        self.assertTrue(expected_duration_min <= duration <= expected_duration_max, "A taxa de envio não corresponde à esperada.")

if __name__ == '__main__':
    unittest.main()
