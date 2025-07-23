import requests
import pandas as pd
from datetime import datetime

# Cotação do dólar (exemplo fixo: 1 USD = 5.40 BRL)
cotacao_dolar = 5.40

# CoinGecko API URL - Bitcoin (últimos 7 dias)
url = "https://api.coingecko.com/api/v3/coins/bitcoin/market_chart"
params = {
    "vs_currency": "usd",
    "days": "7",  # últimos 7 dias
    "interval": "daily"
}

# Requisição
response = requests.get(url, params=params)
data = response.json()

# Extraindo dados de preços
precos = data['prices']

# Formatando dados
dados_formatados = []
for timestamp, price_usd in precos:
    data_formatada = datetime.fromtimestamp(timestamp / 1000).strftime('%d/%m/%Y')
    preco_brl = round(price_usd * cotacao_dolar, 2)
    dados_formatados.append({
        "Data": data_formatada,
        "Preço USD": round(price_usd, 2),
        "Preço BRL": preco_brl
    })

# Criar DataFrame
df = pd.DataFrame(dados_formatados)

# Salvar em CSV
df.to_csv("bitcoin_ultimos_7_dias.csv", index=False, sep=';')

print("Dados salvos com sucesso em 'bitcoin_ultimos_7_dias.csv'")
