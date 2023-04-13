notas = []
media = []
alunosAprovado = 0

for x in range(10):
    nota1 = float(input("1° Nota:"))
    nota2 = float(input("2° Nota:"))
    nota3 = float(input("3° Nota:"))
    nota4 = float(input("4° Nota:"))
    notas.append([nota1, nota2, nota3, nota4])
    mediaAluno = (nota1 + nota2 + nota3 + nota4) / 4
    media.append(mediaAluno)
    if mediaAluno >= 7.0:
        alunosAprovado += 1

print(f"Alunos na Média ou Acima: {alunosAprovado}")