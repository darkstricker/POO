class Pessoa:
    cargo = 'usuario'

    def __init__(self, nome, cpf, altura):
        self.cpf = cpf
        self.altura = altura
        self.nome = nome


class Secretaria(Pessoa):

    def __init__(self, id_secretaria, nome, cpf, altura):
        super().__init__(nome, cpf, altura)
        self.id_secretaria = id_secretaria

class Vendedor(Pessoa):

    def __init__(self, total_vendas, nome, cpf, altura):
        super().__init__(nome, cpf, altura)
        total_vendas += 10
        self.total_vendas = total_vendas
