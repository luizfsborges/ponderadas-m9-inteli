# Baseado em: https://github.com/lvgalvao/One-Billion-Row-Challenge-Python/blob/main/src/using_dask.py

import dask.dataframe as dd
import dask.distributed as distributed

def calculate_temperatures(parquet_file):
    # Configure o ambiente do Dask
    client = distributed.Client()
    
    # Carregue o arquivo Parquet
    df = dd.read_parquet(parquet_file)
    
    # Agrupe por cidade ('City') e calcule a temperatura mínima, média e máxima
    grouped_df = df.groupby('City')['Temperature_Celsius'].agg(['min', 'mean', 'max']).reset_index()
    
    # Compute o resultado
    result_df = grouped_df.compute()
    
    return result_df

if __name__ == "__main__":
    import time

    start_time = time.time()
    
    # Especifique o caminho para o arquivo Parquet
    parquet_file = 'dados_meteorologicos.parquet'
    
    # Execute a função para calcular as temperaturas
    result_df = calculate_temperatures(parquet_file)
    
    took = time.time() - start_time

    print(result_df)
    print(f"Dask Took: {took:.2f} sec")