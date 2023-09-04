alunas = []
alunos = []

while True:
    sexo = input("Digite o sexo do aluno (M ou F) ou 0 para sair: ")
    if sexo == "0":
        break
    altura = float(input("Digite a altura do aluno em metros: "))
    if sexo == "F":
        alunas.append(altura)
    else:
        alunos.append(altura)

if len(alunas) > 0:
    media_alunas = sum(alunas) / len(alunas)
    print("A altura média das alunas é:", media_alunas, "metros.")
else:
    print("Não foram digitadas alturas de alunas.")

if len(alunos) > 0:
    media_alunos = sum(alunos) / len(alunos)
    print("A altura média dos alunos é:", media_alunos, "metros.")
else:
    print("Não foram digitadas alturas de alunos.")