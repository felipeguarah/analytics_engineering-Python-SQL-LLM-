# Python - Pipeline de Carga de Dados

# Imports
import psycopg2
import pandas as pd
from sqlalchemy import create_engine

from dotenv import load_dotenv
import os
from pathlib import Path

load_dotenv()

base_path = Path(os.getenv("BASE_PATH"))
caminho_csv = base_path / "dsa_clientes.csv"



# Cria o motor de conexão (ATENÇÃO COM A STRING DE CONEXÃO ABAIXO!!!!!!)
engine = create_engine('postgresql+psycopg2://dsa:dsa1010@localhost:5959/dsadb')

print("\nIniciando o Processo de Carga dos Dados!\n")

# Função para carregar dados dos arquivos CSV para o PostgreSQL no schema especificado
def dsa_carrega_dados(csv_file, table_name, schema):

    # Bloco try/except
    try:

        # Lê o arquivo CSV
        df = pd.read_csv(csv_file)

        # Executa SQL a partir do dataframe do Pandas
        df.to_sql(table_name, engine, schema = schema, if_exists = 'append', index = False)
        print(f"Dados do arquivo {csv_file} foram inseridos na tabela {schema}.{table_name}.")

    except Exception as e:
        print(f"Erro ao inserir dados do arquivo {csv_file} na tabela {schema}.{table_name}: {e}")

# Carregamento dos dados no schema 'lab5'
dsa_carrega_dados(caminho_csv, 'clientes', 'lab5')
dsa_carrega_dados(caminho_csv, 'produtos', 'lab5')
dsa_carrega_dados(caminho_csv, 'compras', 'lab5')
#dsa_carrega_dados('/Volumes/HD/DataScience_Academy/Cap12/dsa_clientes.csv', 'clientes', 'lab5')
#dsa_carrega_dados('/Volumes/HD/DataScience_Academy/Cap12/dsa_produtos.csv', 'produtos', 'lab5')
#dsa_carrega_dados('/Volumes/HD/DataScience_Academy/Cap12/dsa_compras.csv', 'compras', 'lab5')

print("\nCarga Executada com Sucesso! Use o pgAdmin Para Checar os Dados Se Desejar!\n")