import requests
import jsons

def main():
    cambio_dolar()
    cambio_libra()
    cambio_soles()
    cambio_euro()

def cambio_dolar():
    print("estabelecendo conexão com link...")
    response = requests.get("http://data.fixer.io/api/latest?access_key=1ba0d8f4dfac0e2b0aa76a563e2ae395&format=1")
    if response.status_code == 200:
        print("conseguiu se conectar...")
        dados = response.json()
        taxa_usd = dados['rates']['USD']
        taxa_br = dados['rates']['BRL']
        real = taxa_br / taxa_usd
        print("US$1 custa R$%.2f" % real)
        return real
    else:
        print("site com problema!")

def cambio_euro():
    print("estabelecendo conexão com link...")
    response = requests.get("http://data.fixer.io/api/latest?access_key=1ba0d8f4dfac0e2b0aa76a563e2ae395&format=1")
    if response.status_code == 200:
        print("conseguiu se conectar...")
        dados = response.json()
        taxa_br = dados['rates']['BRL']
        taxa_eu = dados['rates']['EUR']
        euro = taxa_br / taxa_eu
        print("€1 custa R$%.2f" % euro)
        return euro
    else:
        print("site com problema!")

def cambio_libra():
    print("estabelecendo conexão com link...")
    response = requests.get("http://data.fixer.io/api/latest?access_key=1ba0d8f4dfac0e2b0aa76a563e2ae395&format=1")
    if response.status_code == 200:
        print("conseguiu se conectar...")
        dados = response.json()
        taxa_br = dados['rates']['BRL']
        taxa_lb = dados['rates']['GBP']
        libra = taxa_br / taxa_lb
        print("£1 custa R$%.2f" % libra)
        return libra
    else:
        print("site com problema!")

def cambio_soles():
    print("estabelecendo conexão com link...")
    response = requests.get("http://data.fixer.io/api/latest?access_key=1ba0d8f4dfac0e2b0aa76a563e2ae395&format=1")
    if response.status_code == 200:
        print("conseguiu se conectar...")
        dados = response.json()
        taxa_br = dados['rates']['BRL']
        taxa_pe = dados['rates']['PEN']
        peru = taxa_br / taxa_pe
        print("S/1 soles custa R$%.2f" % peru)
        return peru
    else:
        print("site com problema!")

if __name__ == '__main__':
    main()