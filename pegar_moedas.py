import xmltodict

def nomes_moedas():
    with open('moedas.xml', "rb") as arquivos_moedas:
        dict_moedas = xmltodict.parse(arquivos_moedas)
        
    moedas = dict_moedas['xml']  # Certifique-se de que 'xml' é a tag correta no seu XML.
    return moedas  # Retorne as moedas em vez de apenas imprimi-las

# Exemplo de uso da função
moedas_disponiveis = nomes_moedas()
print(moedas_disponiveis)

# Lendo o arquivo de conversões
def conversoes_disponiveis():
    with open('conversoes.xml', 'rb') as arquivos_conversoes:
        dict_conversoes = xmltodict.parse(arquivos_conversoes)

    conversoes = dict_conversoes['xml']  # Provavelmente, deveria ser 'xml' e não 'xlm'
    dict_conversoes_disponiveis = {}
    for par_conversao in conversoes:
        moeda_origem, moeda_destino = par_conversao.split("-")
        if moeda_origem in dict_conversoes_disponiveis:
            dict_conversoes_disponiveis[moeda_origem].append(moeda_destino)
        else:
            dict_conversoes_disponiveis[moeda_origem] = [moeda_destino]
    return(dict_conversoes_disponiveis)        


