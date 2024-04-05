import pandas as pd
import numpy as np
from faker import Faker

# Crie um Faker para gerar dados falsos
fake = Faker()

# Defina o número de linhas a serem geradas (um bilhão neste caso)
num_rows = 1000000000

# Crie uma lista de nomes de cidades fictícias
cities = [fake.city() for _ in range(num_rows)]

# Gere temperaturas aleatórias entre -20 e 40 graus Celsius
temperatures = np.random.uniform(-20, 40, num_rows)

# Crie um DataFrame com os dados gerados
df = pd.DataFrame({'City': cities, 'Temperature_Celsius': temperatures})

# Salve o DataFrame em um arquivo Parquet
df.to_parquet('dados_meteorologicos_cidades.parquet', engine='pyarrow')