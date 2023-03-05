combustível = int(input("Digite uma quantidade de combustível (Máx 30): "))

if combustível > 30:
    int(input("Digite um valor válido: "))

Km = int(input("diga quantos Km quer dirigir: "))

if Km * 2 <= combustível:
    print("Viajem bem sucedida!")
else:
    print("Acabou a gasolina!")
