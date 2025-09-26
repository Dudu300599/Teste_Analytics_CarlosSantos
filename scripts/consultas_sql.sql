-- Assumindo que o arquivo data_clean.csv foi carregado em uma tabela chamada 'Vendas'
-- com as seguintes colunas: ID, Data, Produto, Categoria, Quantidade, Preco





-- Consulta 1: Listar o nome do produto, categoria e a soma total de vendas para cada produto.
-- Ordene o resultado pelo valor total de vendas em ordem decrescente.

/*
Nessa consulta, queremos listar o nome do produto, sua categoria e o total de vendas de cada um. Para isso, 
primeiro selecionamos as colunas Produto e Categoria, que são as que queremos agrupar. Em seguida, calculamos
o total de vendas multiplicando a quantidade pelo preço de cada item e somamos esses valores com a função SUM(),
nomeando o resultado como TotalVendas para deixar claro o que está sendo exibido. Os dados vêm da tabela Vendas,
e agrupamos por produto e categoria para que a soma seja feita corretamente para cada item individual. Por fim, 
ordenamos o resultado de forma decrescente pelo total de vendas, mostrando primeiro os produtos que mais venderam.
*/

SELECT
    Produto,
    Categoria,
    SUM(Quantidade * Preco) AS TotalVendas
FROM
    Vendas
GROUP BY
    Produto, Categoria
ORDER BY
    TotalVendas DESC;


-- Consulta 2: Identificar os produtos que venderam menos no mês de junho de 2023.

/*
Nessa consulta, queremos identificar os produtos que venderam menos durante o mês de junho de 2023. 
Primeiro, selecionamos a coluna Produto e calculamos o total de vendas multiplicando a quantidade pelo 
preço de cada item, nomeando o resultado como VendasJunho. Os dados vêm da tabela Vendas. Para garantir 
que estamos analisando apenas o mês de junho de 2023, usamos o WHERE com a função strftime('%Y-%m', Data) 
para extrair o ano e o mês da coluna de datas e comparamos com '2023-06'. Depois, agrupamos os resultados por produto, 
para que todas as vendas do mesmo item dentro do mês sejam somadas corretamente. Por fim, ordenamos os resultados em 
ordem crescente pelo total de vendas, de forma que os produtos que venderam menos apareçam primeiro.
*/

SELECT
    Produto,
    SUM(Quantidade * Preco) AS VendasJunho
FROM
    Vendas
WHERE
    strftime('%Y-%m', Data) = '2023-06'
GROUP BY
    Produto
ORDER BY
    VendasJunho ASC;