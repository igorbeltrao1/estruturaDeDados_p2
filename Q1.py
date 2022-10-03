grade1 = float(input("Digite a primeira nota do aluno: "))
grade2 = float(input("Digite a segunda nota do aluno: "))
grade3 = float(input("Digite a terceira nota do aluno: "))

media = ((grade1 + grade2 + grade3)/3)

print(f"a média do aluno foi {media}")

if media > 7 and media <10:
    print("Aprovado")
elif media < 7:
    print("Reprovado")
elif media == 10:
    print("Aprovado com distinção")
elif media > 10:
    print("Média inválida. Tente novamente")

