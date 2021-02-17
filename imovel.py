from urllib import parse

class Imovel:

    def __init__(self, endereco, bairro, descricao, preco, cidade, estado, desconto, modalidade_venda):
        self.endereco = endereco
        self.bairro = bairro
        self.descricao = descricao
        self.preco = float(preco.replace(".", "",).replace(",", "."))
        self.cidade = cidade
        self.estado = estado
        self.desconto = float(desconto)
        self.modalidade_venda = modalidade_venda

    def __str__(self):
        return "{0}, {1}, {2}, {3}".format({self.endereco}, {self.bairro}, {self.cidade}, {self.estado})

    def __repr__(self):
        return self.__str__()

    def get_google_maps(self):
        return "https://www.google.com.br/maps/place/{0}".format(parse.quote_plus(self.endereco))
