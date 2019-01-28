import requests
import jsons
import pandas as pd

def main():
    dolar = cambio_dolar()
    euro = cambio_euro()
    libra = cambio_libra()
    soles = cambio_soles()
    exportar_csv(dolar, euro, libra, soles)

def cambio_dolar(url = "http://data.fixer.io/api/latest?access_key=1ba0d8f4dfac0e2b0aa76a563e2ae395&format=1"):
    print("estabelecendo conexão com link...")
    response = requests.get(url)
    if response.status_code == 200:
        dados = response.json()
        taxa_usd = dados['rates']['USD']
        taxa_br = dados['rates']['BRL']
        dolar = taxa_br / taxa_usd
        print("US$1 custa R$%.2f" % dolar)
        return dolar
    else:
        print("site com problema!")

def cambio_euro(url = "http://data.fixer.io/api/latest?access_key=1ba0d8f4dfac0e2b0aa76a563e2ae395&format=1"):
    response = requests.get(url)
    if response.status_code == 200:
        dados = response.json()
        taxa_br = dados['rates']['BRL']
        taxa_eu = dados['rates']['EUR']
        euro = taxa_br / taxa_eu
        print("€1 custa R$%.2f" % euro)
        return euro
    else:
        print("site com problema!")

def cambio_libra(url = "http://data.fixer.io/api/latest?access_key=1ba0d8f4dfac0e2b0aa76a563e2ae395&format=1"):
    response = requests.get(url)
    if response.status_code == 200:
        dados = response.json()
        taxa_br = dados['rates']['BRL']
        taxa_lb = dados['rates']['GBP']
        libra = taxa_br / taxa_lb
        print("£1 custa R$%.2f" % libra)
        return libra
    else:
        print("site com problema!")

def cambio_soles(url = "http://data.fixer.io/api/latest?access_key=1ba0d8f4dfac0e2b0aa76a563e2ae395&format=1"):
    response = requests.get(url)
    if response.status_code == 200:
        dados = response.json()
        taxa_br = dados['rates']['BRL']
        taxa_pe = dados['rates']['PEN']
        soles = taxa_br / taxa_pe
        print("S/1 soles custa R$%.2f" % soles)
        return soles
    else:
        print("site com problema!")
def exportar_csv(dolar, euro, libra, soles):
    linha = {'Dolar - USD': [dolar], 'Euro - EUR': [euro], 'Libra - GBP': [libra], 'Soles - S': [soles]}
    frame = pd.DataFrame(linha, columns = ['Dolar - USD', 'Euro - EUR', 'Libra - GBP', 'Soles - S'])
    frame.to_csv('moeda.csv')
    print("Dados salvos na tabela")

if __name__ == '__main__':
    main()