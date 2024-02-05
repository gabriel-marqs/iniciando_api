import requests

def obter_cotacao(moeda):
    url = "https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        cotacao = data[moeda]['bid']
        return float(cotacao)
    except requests.RequestException as e:
        print(f'Erro ao obter a cotação: {e}')
        return None

cotacao_dolar = obter_cotacao('USDBRL')
cotacao_euro = obter_cotacao('EURBRL')
cotacao_bitcoin = obter_cotacao('BTCBRL')

print(f'Cotação do dólar: {cotacao_dolar:.2f}')
print(f'Cotação do euro: {cotacao_euro:.2f}')
print(f'Cotação do bitcoin: {cotacao_bitcoin:.2f}')