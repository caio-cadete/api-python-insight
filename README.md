API Bitcoin - Coleta de Dados
Este projeto tem como objetivo coletar e salvar dados históricos do preço do Bitcoin utilizando uma API pública, para fins de análise e visualização.

Descrição
Conexão com a API pública CoinGecko para obter dados de preços do Bitcoin.

Extração dos dados de preço diário dos últimos 7 dias (pode ser configurado para outros períodos).

Conversão dos timestamps da API para datas legíveis no formato dd/mm/yyyy.

Conversão do preço do Bitcoin de dólares (USD) para reais (BRL), utilizando uma taxa de câmbio fixa (exemplo: R$ 5,40 por dólar).

Armazenamento dos dados em um arquivo CSV, contendo as colunas:

Data

Preço em USD

Preço em BRL

Tecnologias utilizadas
Python 3

Bibliotecas: requests, pandas, datetime
