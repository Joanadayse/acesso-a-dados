def padronizar_conteudo_gordura(df):
    """Padroniza a coluna 'item_conteudo_gordura' para apenas duas categorias"""
    mapeamento = {
        'Baixo Teor de Gordura': 'Baixo Teor de Gordura',
        'BTG': 'Baixo Teor de Gordura',
        'baixo teor de gordura': 'Baixo Teor de Gordura',
        'Regular': 'Regular',
        'reg': 'Regular'
    }
    df["item_conteudo_gordura"] = df["item_conteudo_gordura"].map(mapeamento)
    print(df["item_conteudo_gordura"].unique())
    return df
