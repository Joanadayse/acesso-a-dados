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
print(df)