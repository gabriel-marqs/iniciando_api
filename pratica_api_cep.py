import requests

def obter_endereco(cep, numero):
    url = 'https://cep.awesomeapi.com.br/json/' + cep
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        rua = data['address_type'] + ' ' + data['address_name']
        bairro = data['district']
        cidade = data['city']
        estado = data['state']
        endereco_completo = f'{rua}, {numero}, {bairro}, {cidade}-{estado} {cep}'
        return endereco_completo
    except requests.RequestException as e:
        print(f'Erro ao obter endereço: {e}')
        return None
   
cep = input('Informe seu cep: ')
numero = input('Informe o número da residência: ')

print(obter_endereco(cep, numero))