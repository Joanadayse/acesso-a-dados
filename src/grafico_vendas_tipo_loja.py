import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def grafico_vendas_tipo_loja(df):
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
    plt.show()