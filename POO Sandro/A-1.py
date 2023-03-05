class Carro:
    def __init__(self, modelo, marca, ano, cor, placa):
        self.self = self
        self.modelo = modelo
        self.marca = marca
        self.ano = ano
        self.cor = cor
        self.placa = placa

    def acelerar(self):
        print("O carro está acelerando.")

    def frear(self):
        print("O carro está freando.")

meu_carro = Carro("toreto", "dodge_charger", 1972, "vermelho", "12131ewqe")

print(meu_carro.modelo)

meu_carro.acelerar()

fusca = Carro("fusca" "" "tartaruga", "volksvagen", 1972, "amarelo", "6C 2625L")

print(fusca.self)
print(fusca.modelo)
print(fusca.marca)
print(fusca.ano)
print(fusca.cor)
print(fusca.placa)