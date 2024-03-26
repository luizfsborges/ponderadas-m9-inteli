# Ponderada 2 - Testes

Esta ponderada tem como objetivo desenvolver testes automatizados para um simulador de dispositivos IoT. Os testes são implementados utilizando o conceito de Test-Driven Development (TDD) para garantir a eficácia e a qualidade do simulador. Os aspectos críticos abordados pelos testes incluem o recebimento e a validação dos dados enviados pelo simulador, além da confirmação da taxa de disparo de mensagens de acordo com as especificações.

## Tecnologias Utilizadas

- **Linguagem de Programação:** Python
- **Biblioteca MQTT:** Eclipse Paho MQTT Python Client
- **Framework de Teste:** unittest (Python Standard Library)

## Instalação e Configuração

### Clonar o Repositório

Para obter o código do projeto, incluindo o simulador e os testes, clone o repositório do GitHub.

```markdown
git clone https://github.com/seu-usuario/nome-do-repositorio.git
cd nome-do-repositorio
```

### Configuração do Ambiente Virtual

É recomendável utilizar um ambiente virtual para instalar as dependências necessárias. Para isso, siga os passos abaixo:

```markdown
python3 -m venv venv
source venv/bin/activate
```

## Funcionalidades Principais

1. **Configuração do Subscriber para Testes** - A função `setup_subscriber` configura o cliente MQTT para atuar como subscriber, armazenando as mensagens recebidas para validação posterior nos testes.

```python
def setup_subscriber():
    def on_message(client, userdata, message):
        received_messages.append(message.payload.decode())

    subscriber = mqtt.Client()
    subscriber.on_message = on_message
    subscriber.connect(broker, port)
    subscriber.subscribe(topic)
    subscriber.loop_start()
    return subscriber
```

2. **Teste de Recebimento dos Dados** - O método `test_data_reception` verifica se uma mensagem enviada pelo publisher é corretamente recebida pelo broker.

```python
def test_data_reception(self):
    test_message = "Test message"
    publisher.publish(topic, test_message)
    time.sleep(2)
    self.assertIn(test_message, received_messages)
```

3. **Teste de Validação dos Dados** - O método `test_data_validation` assegura que os dados recebidos correspondem exatamente aos dados enviados.

```python
def test_data_validation(self):
    self.assertEqual(received_messages[-1], "Test message")
```

4. **Teste da Taxa de Disparo de Mensagens** - O método `test_message_dispatch_rate` valida se o simulador está disparando mensagens dentro da taxa especificada.

```python
def test_message_dispatch_rate(self):
    start_time = time.time()
    for _ in range(2):
        publisher.publish(topic, "Rate test message")
        time.sleep(5)
    duration = time.time() - start_time
    self.assertTrue(9 <= duration <= 11)
```

## Execução dos testes

Para executar os testes automatizados e garantir o funcionamento do simulador, utilize o seguinte comando:

```markdown
pytest
```

Este comando busca e executa todos os testes dentro do diretório especificado, assegurando que todas as funcionalidades do simulador sejam testadas de acordo com os critérios estabelecidos.

## Resultado esperado

<img width="959" alt="pond2" src="https://github.com/luizfsborges/ponderadas-m9-inteli/assets/40524905/e1a81315-eaa6-4832-a328-5b47ff27e73e">
