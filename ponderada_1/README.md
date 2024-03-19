# Ponderada 1 - Simulador MQQ 

Este projeto simula sensores gerando dados aleatórios e publicando-os em um Broker MQTT. Também inclui um subscriber para receber e exibir os dados de forma elegante no terminal.

## Sensor de Radiação Solar Sem Fio HOBOnet RXW-LIB-900

O sensor de radiação solar sem fio HOBOnet RXW-LIB-900 é uma ferramenta avançada para medição de radiação solar em aplicações meteorológicas e ambientais. Ele é calibrado especificamente para medir a intensidade de luz em frequências relevantes para a radiação solar. Esses sensores sem fio são parte integrante do sistema HOBOnet, que permite a transmissão direta de dados para a estação meteorológica RX3000 ou através de outros sensores sem fio para a estação central.

Este sensor é especialmente útil em pesquisas científicas, monitoramento ambiental, agricultura de precisão e aplicações meteorológicas. Seus dados são acessíveis por meio do HOBOlink, uma plataforma de software baseada em nuvem da Onset que permite o gerenciamento e análise dos dados de forma eficiente e acessível.

Para mais informações sobre o sensor de radiação solar sem fio HOBOnet RXW-LIB-900, visite o [site oficial da Sigma Sensors](https://sigmasensors.com.br/produtos/sensor-de-radiacao-solar-sem-fio-hobonet-rxw-lib-900).

## Instalação do Broker MQTT - Mosquitto Eclipse

1. **Linux (Ubuntu):**

   - Abra o terminal e execute o comando:
     ```
     sudo apt update
     sudo apt install mosquitto
     ```
   - Crie o arquivo de configuração `mosquitto.conf` com o seguinte conteúdo:
     ```
     listener 1891
     allow_anonymous true
     ```
   - Inicie o Mosquitto com o arquivo de configuração:
     ```
     mosquitto -c mosquitto.conf
     ```
2. **Windows:**

   - Baixe o instalador do Mosquitto [aqui](https://mosquitto.org/download/).
   - Siga as instruções do instalador para concluir a instalação.
3. **MacOS:**

   - Use o Homebrew para instalar o Mosquitto. No terminal, execute:
     ```
     brew install mosquitto
     ```
   - Siga as instruções para iniciar o serviço do Mosquitto.

## Configuração e Execução do Projeto

1. **Clone o repositório:**

   - Abra o terminal e execute:
     ```
     git clone https://github.com/seu-usuario/nome-do-repositorio.git
     cd nome-do-repositorio
     ```
2. **Instale as dependências Python:**

   - Certifique-se de ter o Python e o gerenciador de pacotes `pip` instalados.
   - Instale as dependências usando o arquivo `requirements.txt`:
     ```
     pip install -r requirements.txt
     ```
3. **Execute o Broker MQTT:**

   - Inicie o serviço do Mosquitto com o arquivo de configuração:
     ```
     mosquitto -c mosquitto.conf
     ```
   - Certifique-se de que o Broker MQTT esteja em execução antes de iniciar o projeto.
4. **Execute o Publisher:**

   - Abra um terminal na pasta do projeto e execute o script `mqtt_solar_publisher.py`:
     ```
     python mqtt_solar_publisher.py
     ```
   - Isso iniciará a simulação do sensor de radiação solar HOBOnet e publicará os dados no Broker MQTT.
5. **Execute o Subscriber:**

   - Abra outro terminal na pasta do projeto e execute o script `mqtt_solar_subscriber.py`:
     ```
     python mqtt_solar_subscriber.py
     ```
   - O subscriber se conectará ao Broker MQTT, se inscreverá no tópico "dados_sensor" e exibirá os dados recebidos de forma elegante no terminal.

## Comportamento esperado

Ao executar o Subscriber (`mqtt_solar_subscriber.py`), você deve esperar ver os seguintes dados exibidos no terminal para cada leitura recebida do sensor de radiação solar HOBOnet:

- Sensor ID: RXW-LIB-900
- Latitude: (valor aleatório dentro do intervalo de -90 a 90)°
- Longitude: (valor aleatório dentro do intervalo de -180 a 180)°
- Leitura: (valor aleatório de radiação solar em W/m²)

Os dados serão atualizados conforme o Publisher envia novas leituras, e a exibição será formatada de forma clara e legível para o usuário.

## Vídeo de demonstração

https://github.com/luizfsborges/ponderadas-m9-inteli/assets/40524905/1bfb2443-460e-4867-805e-95a5fbbee7ea



