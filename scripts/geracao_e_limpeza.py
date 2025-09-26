import pandas as pd
import numpy as np
import random
from datetime import date, timedelta


# --- 1. Simulação do Dataset ---
# Definição de parametros
num_registros = 100 # Serão gerados 100 registros.
start_date = date(2023, 1, 1) # Data Inicio
end_date = date(2023, 12, 31) # Data Fim
date_range = (end_date - start_date).days # Intervalo entre Data Inicio de Data Fim

# Listas de possiveis valores para as colunas categorias
produtos_categorias = {
    'Eletrônicos': ['Smartphone', 'Notebook', 'Smartwatch', 'Fone de Ouvido'],
    'Vestuário': ['Camiseta', 'Calça Jeans', 'Tênis'],
    'Casa e Cozinha': ['Cafeteira', 'Liquidificador', 'Panela Elétrica'],
    'Livros': ['Ficção Científica', 'Fantasia', 'Biografia']
}

# Geração dos dados
data = []
for i in range(num_registros):
    categoria = random.choice(list(produtos_categorias.keys()))
    produto = random.choice(produtos_categorias[categoria])
    random_days = random.randint(0, date_range)
    
    data.append({
        'ID': i + 1,
        'Data': start_date + timedelta(days=random_days),
        'Produto': produto,
        'Categoria': categoria,
        'Quantidade': random.randint(1, 15),
        'Preço': round(random.uniform(50.0, 3000.0), 2)
    })

df = pd.DataFrame(data)


# --- Introdução de Imperfeições para Limpeza ---
# Insere valores faltantes (NaN)
for _ in range(5):
    row_idx = random.randint(0, num_registros - 1)
    col_to_null = random.choice(['Quantidade', 'Preço'])
    df.loc[row_idx, col_to_null] = np.nan

# Insere linhas duplicadas
duplicated_rows = df.sample(n=3)
df = pd.concat([df, duplicated_rows]).reset_index(drop=True)

# Salva Arquivo sem tratamento
df.to_csv('data/data_raw.csv', index=False, encoding='utf-8')

# --- 2. Limpeza dos Dados ---
# Tratamento de valores faltantes
# Para 'Quantidade', usar a mediana, pois é mais robusta a outliers.
median_qty = df['Quantidade'].median()
df['Quantidade'] = df['Quantidade'].fillna(median_qty)

# Para 'Preço', usar a média do preço do produto específico.
# Isso é uma abordagem mais refinada do que a média geral.
df['Preço'] = df.groupby('Produto')['Preço'].transform(lambda x: x.fillna(x.mean()))
# Caso algum produto só tenha NaN, preenche com a média geral como fallback.
df['Preço'] = df['Preço'].fillna(df['Preço'].mean())


# Remoção de duplicatas
num_duplicatas = df.duplicated().sum()
df.drop_duplicates(inplace=True)

# Conversão de tipos de dados
df['Data'] = pd.to_datetime(df['Data'])
df['Quantidade'] = df['Quantidade'].astype(int) # Garante que seja inteiro após o fillna



# --- 3. Salvar o Dataset Limpo ---
df.to_csv('data/data_clean.csv', index=False, encoding='utf-8')


# --- 4. Análise de Vendas ---
# Calcula o total de vendas por transação
df['TotalVendas'] = df['Quantidade'] * df['Preço']

# Calcula o total de vendas por produto
vendas_por_produto = df.groupby('Produto')['TotalVendas'].sum().sort_values(ascending=False)
print("\nTotal de Vendas por Produto:")
print(vendas_por_produto)

# Salva total de vendas por produto
vendas_por_produto_df = vendas_por_produto.reset_index()
vendas_por_produto_df.rename(columns={'TotalVendas':'TotalVenda'}, inplace=True)

vendas_por_produto_df.to_csv("data/total_vendas_por_produto.csv", index=False, encoding="utf-8")
print("Total de vendas por produto salvo em 'data/total_vendas_por_produto.csv'.")

# Identifica o produto com maior número de vendas totais
produto_mais_vendido = vendas_por_produto.idxmax()
valor_mais_vendido = vendas_por_produto.max()

print(f"\nO produto com o maior total de vendas é '{produto_mais_vendido}' com um total de R$ {valor_mais_vendido:,.2f}.")