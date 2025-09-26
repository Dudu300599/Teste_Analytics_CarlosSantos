import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.dates as mdates
import locale
from datetime import date


locale.setlocale(locale.LC_TIME, 'Portuguese_Brazil.1252')
print("Iniciando a análise exploratória...")

# Carregar o dataset limpo
try:
    df = pd.read_csv('data/data_clean.csv', parse_dates=['Data'])
except FileNotFoundError:
    print("Erro: O arquivo 'data/data_clean.csv' não foi encontrado.")
    print("Execute o script 'geracao_e_limpeza.py' primeiro.")
    exit()

# Calcula a coluna 'TotalVendas' para uso nas análises deste script
df['TotalVendas'] = df['Quantidade'] * df['Preço']

# --- 1. Gráfico de Tendência de Vendas Mensais ---
# Define a coluna 'Data' como indice para facilitar a agregação por tempo
df_time = df.set_index('Data')

# Agrupa os dados por mês 'MS' e soma o total de vendas
vendas_mensais = df_time['TotalVendas'].resample('MS').sum()

#Filtra meses com venda
vendas_mensais = vendas_mensais[vendas_mensais > 0]

# Cria o gráfico
plt.style.use('seaborn-v0_8-whitegrid')
fig, ax = plt.subplots(figsize=(12, 6))

ax.plot(vendas_mensais.index, vendas_mensais.values, marker='o', linestyle='-')
ax.set_title('Tendência de Vendas Mensais (2023)', fontsize=16)
ax.set_xlabel('Mês', fontsize=12)
ax.set_ylabel('Total de Vendas (R$)', fontsize=12)
plt.gca().ticklabel_format(style='plain', axis='y') # Evita notação científica

# Formataro eixo X para mostrar os meses de forma legível
ax.xaxis.set_major_locator(mdates.MonthLocator()) 
plt.xticks(rotation=45)
plt.tight_layout()

# Salva o gráfico
plt.savefig('relatorio/tendencia_vendas_mensais.png')


# --- 2. Identificação de Padrões e Insights ---
print("\n--- Insights Observados ---")

# Insight 1: Sazonalidade das Vendas
mes_maior_venda = vendas_mensais.idxmax()
mes_menor_venda = vendas_mensais.idxmin()
print(f"Insight 1: Sazonalidade.")
print(f"Os dados mostram um comportamento sazonal, com picos e vales ao longo do ano.")
print(f"O mês de maior faturamento foi {mes_maior_venda.strftime('%B de %Y')}, enquanto o de menor faturamento foi {mes_menor_venda.strftime('%B de %Y')}.")
print("Isso pode estar relacionado a datas comemorativas, férias ou eventos específicos. A flutuação aleatória dos dados simulados pode gerar diferentes padrões a cada execução.")

# Insight 2: Concentração de Receita em Poucas Categorias/Produtos
vendas_por_categoria = df.groupby('Categoria')['TotalVendas'].sum().sort_values(ascending=False)
porcentagem_top_categoria = (vendas_por_categoria.iloc[0] / vendas_por_categoria.sum()) * 100

print(f"\nInsight 2: Concentração de Receita.")
print("Observa-se uma concentração significativa de receita em poucas categorias. A categoria de maior faturamento, "
      f"'{vendas_por_categoria.index[0]}', foi responsável por {porcentagem_top_categoria:.2f}% do total das vendas.")
print("Isso sugere que certos tipos de produtos são os principais motores de receita da empresa.")

# Plotar gráfico de barras para o Insight 2
fig2, ax2 = plt.subplots(figsize=(10, 6))
sns.barplot(x=vendas_por_categoria.values, y=vendas_por_categoria.index, hue=vendas_por_categoria.index, palette='viridis', ax=ax2)
ax2.set_title('Total de Vendas por Categoria', fontsize=16)
ax2.set_xlabel('Total de Vendas (R$)', fontsize=12)
ax2.set_ylabel('Categoria', fontsize=12)
plt.tight_layout()
plt.savefig('relatorio/vendas_por_categoria.png')