import matplotlib.pyplot as plt
import seaborn as sns

def grafico_tipo_de_item(df):
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
    plt.show()
