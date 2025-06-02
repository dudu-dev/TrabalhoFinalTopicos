import yfinance as yf
import os

# Lista dos tickers
tickers = ['AAPL', 'MSFT', 'META', 'GOOGL', 'NVDA']

# Baixa os dados do último ano para todos os tickers
dados = yf.download(tickers, period='1y')

# Seleciona a coluna 'Close' (fechamento simples)
fechamento = dados.xs('Close', axis=1, level=0)

# Nome do arquivo CSV
nome_arquivo = 'fechamento_acoes_ultimo_ano.csv'

# Salva o DataFrame em CSV
fechamento.to_csv(nome_arquivo)

# Imprime o caminho completo do arquivo salvo
caminho_completo = os.path.abspath(nome_arquivo)
print(f"Arquivo salvo em: {caminho_completo}")
