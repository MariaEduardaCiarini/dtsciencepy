# scraper_recr11.py
# Projeto: Web scraping de ativo FII (RECR11.SA) usando yfinance

import yfinance as yf

# Define o ticker do ativo (FII da B3)
ativo = yf.Ticker("RECR11.SA")

# Coleta os dados atuais do ativo
info = ativo.info

# Exibe os dados no terminal
print("Nome do ativo:", info.get("longName"))
print("Preço atual:", info.get("regularMarketPrice"))
print("Variação diária (%):", info.get("regularMarketChangePercent"))
print("Fechamento anterior:", info.get("regularMarketPreviousClose"))

# Salva os dados em um arquivo .txt
with open("dados_recr11.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write(f"Nome do ativo: {info.get('longName')}\n")
    arquivo.write(f"Preço atual: {info.get('regularMarketPrice')}\n")
    arquivo.write(f"Variação diária (%): {info.get('regularMarketChangePercent')}\n")
    arquivo.write(f"Fechamento anterior: {info.get('regularMarketPreviousClose')}\n")
