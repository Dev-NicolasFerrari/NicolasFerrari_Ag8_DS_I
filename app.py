contador = 1
excelente = 0
bom = 0
ruim = 0

while contador <= 50:
    nome = input("Digite o seu nome: ")
    idade = int(input("Digite a sua idade: "))
    nota = int(input("Digite o grau de satisfação no atendimento sendo 1-Exelente, 2-Bom e 3-Ruim: "))
    if nota == 1:
        print("Sua nota foi Excelente!")
        contador += 1
        excelente += 1
        print("Contagem de notas: ", excelente, " Excelente, ", bom, " Bom e ", ruim, " Ruim!")
    elif nota == 2:
        print("Sua nota foi Bom!")
        contador += 1
        bom += 1
        print("Contagem de notas: ", excelente, " Excelente, ", bom, " Bom e ", ruim, " Ruim!")
    elif nota == 3:
        print("Sua nota foi Ruim!")
        contador += 1
        ruim += 1
        print("Contagem de notas: ", excelente, " Excelente, ", bom, " Bom e ", ruim, " Ruim!")
    else:
        print("Nota não existente!")