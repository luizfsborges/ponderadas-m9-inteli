# Ponderada 4 - Testes Automatizados de MQTT com Paho

## Introdução

Este documento descreve os testes automatizados realizados para verificar a funcionalidade de um simulador MQTT usando a biblioteca Paho MQTT. O simulador é projetado para simular um sensor de qualidade do ar (SPS30) e se conectar a um broker HiveMQ para publicar dados e validar sua integração.

### Passo a Passo:

1. Clone o repositório:
```
   git clone <https://github.com/nome-do-repositorio>
    cd <ponderada_4>
```
2. Instale as dependências
```
pip install .
```
3. Faça um Cluster no serviço HiveMQ e registre suas credenciais de acesso em um arquivo .env
  
```
MQTT_BROKER="y0e23a3db3b6347278db0afe6d844d5ed.s1.eu.hivemq.cloud"
MQTT_PORT=8883
MQTT_TOPIC="dados_sensor"
MQTT_CLIENT_ID_PUBLISHER="python_publisher_test"
MQTT_CLIENT_ID_SUBSCRIBER="python_subscriber_test"
MQTT_USERNAME="USERNAME"
MQTT_PASSWORD="PASSWORD"
```

## Configuração

Os testes são configurados para se conectar a um broker MQTT usando os parâmetros fornecidos por variáveis de ambiente. As variáveis de ambiente incluem o endereço do broker, porta, tópico MQTT, IDs do cliente para publicação e subscrição, nome de usuário e senha.

As credenciais e parâmetros de conexão são carregados a partir de um arquivo .env usando a biblioteca `dotenv`.

## Estrutura de Testes

Os testes são organizados em uma classe `TestIoTSimulator` que herda da classe `unittest.TestCase`. A configuração inicial dos testes inclui a criação de clientes MQTT para publicação e subscrição, aplicando configurações de TLS e autenticação usando as credenciais fornecidas.

Os testes incluem as seguintes funcionalidades e funções:

### 1. `test_data_reception()`

Este teste verifica se os dados podem ser recebidos corretamente pelo broker MQTT. Ele publica uma mensagem de teste no tópico MQTT configurado e aguarda 2 segundos para garantir a recepção da mensagem pelo assinante. Em seguida, verifica se a mensagem de teste foi recebida corretamente.

### 2. `test_data_validation()`

Este teste confirma se os dados recebidos correspondem aos dados enviados. Ele supõe que o teste anterior `test_data_reception()` já adicionou uma mensagem à lista `received_messages` e verifica se a última mensagem recebida corresponde à mensagem enviada.

### 3. `test_message_dispatch_rate()`

Este teste verifica se as mensagens estão sendo enviadas na taxa esperada. Ele publica duas mensagens de teste com um intervalo de 5 segundos entre cada uma e mede o tempo de envio. A taxa de envio esperada é de 1 mensagem a cada 5 segundos, com uma margem de 1 segundo. O teste verifica se a taxa de envio está dentro da faixa esperada.

## Execução dos Testes

### Execução Local

Para executar os testes localmente, utilize o seguinte comando:

```
pytest
```

Isso executará os testes automatizados e fornecerá feedback sobre a integridade e funcionalidade do simulador MQTT.