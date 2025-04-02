import matplotlib.pyplot as plt
import seaborn as sns

def grafico_vendas_conteudo_gordura(df):
    """Cria um gráfico de barras para vendas por conteúdo de gordura"""
    df_agrupado = df.groupby("item_conteudo_gordura")["vendas_totais"].sum().reset_index()
    
    cores = {"Baixo Teor de Gordura": "#e23155", "Regular": "#acdcd3"}
    
    fig, ax = plt.subplots(figsize=(8, 6))
    fig.patch.set_facecolor("#ebebeb")
    ax.set_facecolor("#ebebeb")

    sns.barplot(x="item_conteudo_gordura", y="vendas_totais", data=df_agrupado, palette=cores, ax=ax)

    for index, (categoria, valor) in enumerate(zip(df_agrupado["item_conteudo_gordura"], df_agrupado["vendas_totais"])):
        ax.text(index, valor + 0.02 * valor, f"R$ {valor/1e6:.1f} M", ha="center", color="#19325c", fontsize=12, fontweight="bold")

    ax.set_xlabel("Conteúdo de Gordura", fontsize=12, fontweight="bold", color="#19325c")
    ax.set_ylabel("Total de Vendas", fontsize=12, fontweight="bold", color="#19325c")
    ax.set_title("Total de Vendas por Conteúdo de Gordura", fontsize=14, fontweight="bold", color="#19325c")
    
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_color("#19325c")
    ax.spines["bottom"].set_color("#19325c")
    ax.tick_params(colors="#19325c")

    ax.grid(False)
    plt.show()
