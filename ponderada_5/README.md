# Ponderada 5

# Solução do desafio dos 1 bilhão de linhas usando Desk


O Desafio dos 1 Bilhão de Linhas, também conhecido como 1BLC, é um desafio proposto para testar a capacidade de processamento e manipulação de grandes volumes de dados em formato CSV*. O objetivo é realizar operações eficientes em um arquivo contendo um bilhão de linhas de dados, exigindo técnicas avançadas de processamento e análise de dados em larga escala. Para resolvê-lo, escoljhi utilizar o Desk, que é uma ferramenta de computação paralela e distribuida em Python, projetada para lidar com análise e processamento de grandes conjuntos de dados. Ele facilita a execução de operações em paralelo em vários CPUs ou nós de um cluster, oferecendo escalabilidade, eficiência e capacidade de processamento distribuído para tarefas complexas envolvendo grandes volumes de dados.

*fiz minha implementação em parquert pois não tinha memória o suficiente no meu computador

### Processamento Distribuído

O processamento distribuído, facilitado pela tecnologia Dask, permite que tarefas sejam divididas em partes menores e executadas em várias CPUs ou nós de um cluster de computadores. Isso é especialmente útil para lidar com grandes conjuntos de dados que excedem a capacidade de memória de um único computador, distribuindo a carga de trabalho de forma eficiente entre diversos recursos computacionais.

### Estratégia de "Lazy Loading"

O Dask adota uma estratégia de carregamento preguiçoso, onde as operações não são realizadas imediatamente após serem definidas. Em vez disso, as operações são adiadas até que os resultados sejam necessários. Essa abordagem é benéfica ao lidar com grandes volumes de dados, pois permite otimizar o uso de recursos computacionais e evitar processamento desnecessário.

### Organização de Tarefas

Ao definir operações em um DataFrame ou conjunto de dados no Dask, ele cria um grafo de tarefas que representa a sequência de operações a serem executadas. Esse grafo é uma representação das operações e suas dependências, permitindo uma visão clara da estrutura das tarefas a serem realizadas.

### Computação Sob Demanda

A computação sob demanda é um princípio fundamental do Dask, onde as operações não são executadas automaticamente após serem definidas. Em vez disso, as operações são realizadas apenas quando há uma solicitação explícita para computar os resultados usando o método compute(). Isso ajuda a evitar o processamento desnecessário e a otimizar o uso de recursos.

### Utilização de Paralelismo e Otimização Automática

O Dask utiliza o paralelismo disponível em sistemas distribuídos para executar tarefas de forma eficiente em várias CPUs ou nós de um cluster. Além disso, ele realiza otimizações automáticas, como dividir tarefas maiores em partes menores que podem ser executadas simultaneamente em paralelo. Essas técnicas garantem uma execução eficiente e escalável de operações em grandes conjuntos de dados.
