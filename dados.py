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
# remover as linhas duplicadas
df.drop_duplicates(inplace=True)
# remover coluna com ausencia de dados
df.drop(columns=['item_quantidade_venda'], inplace=True)
# preencher os valores nulos com o valor médio ou mediano da coluna item_peso
df['loja_tamanho'] = df['loja_tamanho'].fillna('Desconhecido')
# Mapeie os valores não padronizados para os valores padronizados
mapeamento = {
    'BTG': 'Baixo Teor de Gordura',
    'reg': 'Regular',
    'baixo teor de gordura': 'Baixo Teor de Gordura'
}
# Aplicando a substituição na coluna
df["item_conteudo_gordura"] = df["item_conteudo_gordura"].replace(mapeamento)
# Verificando os valores únicos após a correção
print(df["item_conteudo_gordura"].unique())

