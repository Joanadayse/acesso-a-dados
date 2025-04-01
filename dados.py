import numpy as np
import pandas as pd
from pandas import json_normalize



url = 'https://github.com/alura-cursos/python-analise-chatgpt-assistente/raw/main/Dados/dados_vendas.json'
df = pd.read_json(url)
# print(df.head())

df_item_normalized= json_normalize(df["item"])
df_loja_normalized = json_normalize(df['loja'])
df = pd.concat([df, df_item_normalized, df_loja_normalized], axis=1)
df.drop(['item', 'loja'], axis=1, inplace=True)
print(df)

# Verificar se há valores únicos em colunas específicas, por exemplo, "item_identificador” e “loja_identificador”
print(df['item_conteudo_gordura'].unique())