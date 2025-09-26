# Teste para Estagiário de Analytics - [Carlos Santos]

Este repositório contém a resolução do teste para a vaga de Estagiário de Analytics na Quod.

## Estrutura do Repositório

O projeto está organizado da seguinte forma:

```
/
│
├── README.md                   # Esta documentação
├── requirements.txt            # Dependências Python para fácil instalação
│
├── data/
│   ├── data_raw.csv                    # Dataset bruto, sem nenhum tratamento. Gerado pelo geracao_e_limpeza.py
│   ├── data_clean.csv                  # Dataset limpo e tratado. Gerado pelo geracao_e_limpeza.py
│   └── total_venda_por_produto         # Dataset com o total de vender por produto. Gerado pelo geracao_e_limpeza.py
│
│
├── scripts/
│   ├── geracao_e_limpeza.py            # Simula, limpa e faz a primeira análise
│   ├── analise_exploratoria.py         # Gera visualizações e insights
│   └── consultas_sql.sql               # Consultas SQL
│
└── relatorio/
    ├── relatorio_insights.md           #Relatório com insights e ações
    ├── tendencia_vendas_mensais.png    # Gráfico gerado pelo analise_exploratoria.py 
    └── vendas_por_categoria.png        # Gráfico gerado pelo analise_exploratoria.py 

```

## Como Executar os Scripts

### Pré-requisitos
- Python 3.8 ou superior
- Git

### Instalação

1.  Clone o repositório:
    ```bash
    git clone [[URL_DO_SEU_REPOSITORIO]](https://github.com/Dudu300599/Teste_Analytics_CarlosSantos)
    cd Teste_Analytics_CarlosSantos
    ```

2.  Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

### Execução

Os scripts devem ser executados na ordem correta, a partir da raiz do projeto:

1.  **Gerar e limpar os dados:**
    ```bash
    python scripts/geracao_e_limpeza.py
    ```
    Este script criará os arquivos `data/data_raw.csv`, `data/data_clean.csv`, `data/total_vendas_por_produto.csv`.

2.  **Realizar a análise exploratória e gerar gráficos:**
    ```bash
    python scripts/analise_exploratoria.py
    ```
    Este script usará o arquivo `data_clean.csv` e salvará os gráficos na pasta `relatorio/`.

## Suposições Feitas

1.  **Dados Simulados:** Os dados de produtos, categorias e preços foram gerados de forma aleatória dentro de intervalos predefinidos para simular um ambiente de e-commerce variado.
2.  **Limpeza de Dados:** Para tratar valores faltantes, optei por preencher a `Quantidade` com a mediana (mais robusta a outliers) e o `Preço` com a média do preço do produto específico (uma abordagem mais precisa que a média geral).
