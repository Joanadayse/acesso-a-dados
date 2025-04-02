import pandas as pd
import requests
from pandas import json_normalize
from io import StringIO



def carrega_dados(url):
    """Carrega os dados do JSON a partir de uma URL e retorna um DataFrame"""
    try:
      
        response = requests.get(url)
        response.raise_for_status()  # Lança um erro se a resposta for inválida
        
        # Usando StringIO para tratar o JSON como um arquivo
        json_data = StringIO(response.text)
        
        # Agora lemos o JSON de maneira mais adequada
        df = pd.read_json(json_data)
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

        print("\n📌 Dados carregados com sucesso!\n")
        
        return df

    except requests.exceptions.RequestException as e:
        print(f"❌ Erro ao acessar a URL: {e}")
    except ValueError as e:
        print(f"❌ Erro ao processar os dados: {e}")
    except Exception as e:
        print(f"❌ Ocorreu um erro inesperado: {e}")

