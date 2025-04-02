from src.carrega_dados import carrega_dados
from src.padronizar_conteudo_gordura import padronizar_conteudo_gordura
from src.grafico_vendas_conteudo_gordura import grafico_vendas_conteudo_gordura



url = 'https://github.com/alura-cursos/python-analise-chatgpt-assistente/raw/main/Dados/dados_vendas.json'
df= carrega_dados(url)

df=padronizar_conteudo_gordura(df)

grafico_vendas_conteudo_gordura(df)
