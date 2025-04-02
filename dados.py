import numpy as np
import pandas as pd
from pandas import json_normalize
import matplotlib.pyplot as plt
import seaborn as sns



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
# print(df["item_conteudo_gordura"].unique())

# Agrupar as vendas por tipo de loja
df_agrupado = df.groupby("loja_tipo")["vendas_totais"].sum().reset_index()

# Ordenar os tipos de loja para manter uma sequência lógica
ordem_lojas = ["Supermercado Tipo 1", "Supermercado Tipo 2", "Supermercado Tipo 3", "Mercado"]
df_agrupado["loja_tipo"] = pd.Categorical(df_agrupado["loja_tipo"], categories=ordem_lojas, ordered=True)
df_agrupado = df_agrupado.sort_values("loja_tipo")

# Criar a figura e definir o fundo
fig, ax = plt.subplots(figsize=(8, 5))
fig.patch.set_facecolor("#ebebeb")  # Fundo da figura
ax.set_facecolor("#ebebeb")  # Fundo do plot

# Criar o gráfico de barras
sns.barplot(
    x="loja_tipo", 
    y="vendas_totais", 
    data=df_agrupado, 
    order=ordem_lojas, 
    color="#e23155",
    ax=ax
)

# Adicionar rótulos nas barras com valores em milhões
for i, valor in enumerate(df_agrupado["vendas_totais"]):
    ax.text(i, valor + 0.05 * valor, f"R$ {valor/1e6:.1f} M", ha="center", color="#19325c", fontsize=12, fontweight="bold")

# Personalizar rótulos e título
ax.set_xlabel("Tipo de Loja", fontsize=12, fontweight="bold", color="#19325c")
ax.set_ylabel("Total de Vendas", fontsize=12, fontweight="bold", color="#19325c")
ax.set_title("Total de Vendas por Tipo de Loja", fontsize=14, fontweight="bold", color="#19325c")
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_color("#19325c")
ax.spines["bottom"].set_color("#19325c")
ax.tick_params(colors="#19325c", rotation=20)  # Rotacionar os rótulos para melhor visualização

# Exibir gráfico
# plt.show()

# Agrupar as vendas por tipo de item e ordenar em ordem decrescente
df_agrupado = df.groupby("item_tipo")["vendas_totais"].sum().reset_index()
df_agrupado = df_agrupado.sort_values("vendas_totais", ascending=True)  # Para funil (menor para maior)

# Criar a figura e definir o fundo
fig, ax = plt.subplots(figsize=(10, 7))
fig.patch.set_facecolor("#ebebeb")  # Fundo da figura
ax.set_facecolor("#ebebeb")  # Fundo do plot

# Criar o gráfico de barras horizontais
sns.barplot(
    y="item_tipo", 
    x="vendas_totais", 
    data=df_agrupado, 
    color="#e23155",
    ax=ax
)

# Adicionar rótulos nas barras com valores em milhões
for index, (valor, tipo) in enumerate(zip(df_agrupado["vendas_totais"], df_agrupado["item_tipo"])):
    ax.text(valor + 0.02 * valor, index, f"R$ {valor/1e6:.1f} M", va="center", color="#19325c", fontsize=12, fontweight="bold")

# Personalizar rótulos e título
ax.set_ylabel("Categoria de Produto", fontsize=12, fontweight="bold", color="#19325c")
ax.set_xlabel("Total de Vendas", fontsize=12, fontweight="bold", color="#19325c")
ax.set_title("Total de Vendas por Categoria de Produto", fontsize=14, fontweight="bold", color="#19325c")
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_color("#19325c")
ax.spines["bottom"].set_color("#19325c")
ax.tick_params(colors="#19325c")

# Remover grid
ax.grid(False)

# Exibir gráfico
# plt.show()


# Agrupar as vendas por conteúdo de gordura
df_agrupado = df.groupby("item_conteudo_gordura")["vendas_totais"].sum().reset_index()

# Definir cores específicas para cada categoria
cores = {"Baixo Teor de Gordura": "#e23155", "Regular": "#acdcd3"}

# Criar a figura e definir o fundo
fig, ax = plt.subplots(figsize=(8, 6))
fig.patch.set_facecolor("#ebebeb")  # Fundo da figura
ax.set_facecolor("#ebebeb")  # Fundo do plot

# Criar o gráfico de colunas
sns.barplot(
    x="item_conteudo_gordura", 
    y="vendas_totais", 
    data=df_agrupado, 
    palette=cores, 
    ax=ax
)

# Adicionar rótulos acima das colunas com valores em milhões
for index, (categoria, valor) in enumerate(zip(df_agrupado["item_conteudo_gordura"], df_agrupado["vendas_totais"])):
    ax.text(index, valor + 0.02 * valor, f"R$ {valor/1e6:.1f} M", ha="center", color="#19325c", fontsize=12, fontweight="bold")

# Personalizar rótulos e título
ax.set_xlabel("Conteúdo de Gordura", fontsize=12, fontweight="bold", color="#19325c")
ax.set_ylabel("Total de Vendas", fontsize=12, fontweight="bold", color="#19325c")
ax.set_title("Total de Vendas por Conteúdo de Gordura", fontsize=14, fontweight="bold", color="#19325c")
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_color("#19325c")
ax.spines["bottom"].set_color("#19325c")
ax.tick_params(colors="#19325c")

# Remover grid
ax.grid(False)

# Exibir gráfico
plt.show()
