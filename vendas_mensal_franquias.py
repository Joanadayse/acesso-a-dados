import pandas as pd
import json
import requests

url_franquias = 'https://raw.githubusercontent.com/alura-cursos/python-analise-chatgpt-assistente/main/Dados/vendas_mensal_franquias.json'

response= requests.get(url_franquias)
dados= response.json()
df=pd.DataFrame(dados)

df_vendas= pd.json_normalize(df['vendas'])
df_loja= pd.json_normalize(df['loja'])

df= pd.concat([df, df_vendas , df_loja], axis=1)
df= df.drop(['vendas', 'loja'], axis=1)

# Verificar as primeiras 5 linhas do DataFrame
# print(df.head())

# Resumo estatístico das colunas numéricas
# print(df.describe())

# info()rmações gerais sobre o DataFrame, incluindo tipos de dados e contagem
# print(df.info())

# Verificar a contagem de valores únicos em cada coluna
# print(df.nunique())

# Verificar se há valores duplicados no DataFrame
# print(df.duplicated().sum())

# Verifique se existem valores ausentes por coluna
# print(df.isnull().sum())

# confirmar as categorias de tamanho_loja
 