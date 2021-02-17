from imovel import Imovel
from bs4 import BeautifulSoup
import requests
lista_de_imoveis = []
html_text = requests.get("https://venda-imoveis.caixa.gov.br/listaweb/Lista_imoveis_RJ.htm").text
soup = BeautifulSoup(html_text, "html.parser")
imoveis = soup.find_all("tr")
del imoveis[0]

for imovel in imoveis:
    endereco = imovel.find_all("td")[1].text.strip()
    bairro = imovel.find_all("td")[2].text.strip()
    descricao = imovel.find_all("td")[3].text.strip()
    preco = imovel.find_all("td")[4].text.strip()
    cidade = imovel.find_all("td")[9].text.strip()
    estado = imovel.find_all("td")[-1].text.strip()
    desconto = imovel.find_all("td")[6].text.strip()
    modalidade_venda = imovel.find_all("td")[7].text.strip()

    obj_imovel = Imovel(endereco, bairro, descricao, preco, cidade, estado, desconto, modalidade_venda)
    lista_de_imoveis.append(obj_imovel)

# print(lista_de_imoveis[1].bairro)

# for imovel in lista_de_imoveis:
#     print(imovel.preco)

print("Cidade")
print("Bairro")
print("Desconto")
print("Modalidade da venda")
pergunta_filtro = input("Pelo o que deseja filtrar ? ").lower()


lista_de_bairros_filtrados = []
for conjunto_de_bairros in lista_de_imoveis:
    lista_de_bairros_filtrados.append(conjunto_de_bairros.bairro)

lista_de_bairros_filtrados = list(set(lista_de_bairros_filtrados))

lista_cidades_filtradas = []
for conjunto_de_cidades in lista_de_imoveis:
    lista_cidades_filtradas.append(conjunto_de_cidades.cidade)

lista_cidades_filtradas = list(set(lista_cidades_filtradas))

while True:
    if pergunta_filtro == "bairro":
        for bairro in lista_de_bairros_filtrados:
            print(bairro)
        pergunta_bairro = input("Qual bairro? ").upper()
        for imovel in lista_de_imoveis:
            if pergunta_bairro == imovel.bairro:
                print(imovel)
                break
    elif pergunta_filtro == "cidade":
        for cidade in lista_cidades_filtradas:
            print(cidade)
        pergunta_cidade = input("Qual cidade ? ").upper()
        for imovel in lista_de_imoveis:
            if pergunta_cidade == imovel.cidade:
                print(imovel)
                break
    elif pergunta_filtro == "desconto":
        pergunta_desconto = float(input("Deseja descontos apartir de ? "))
        for imovel in lista_de_imoveis:
            if imovel.desconto >= pergunta_desconto:
                print(imovel)
                break
    elif pergunta_filtro == "modalidade de venda":
        print("Venda Direta Online ou Venda Direta")
        pergunta_modalidade_de_venda = input("Deseja qual modalidade de venda? ")
        for imovel in lista_de_imoveis:
            if pergunta_modalidade_de_venda == imovel.modalidade_venda:
                print(imovel)
                break
    else:
        print('Digite um bairro ou cidade.')
