num = 1

while num !=0:
  num = int(input("Digite a primeira nota de zero a dez: "))

  if num > 10:
    print("Nota inválida. Tente novamente")
  if num < 0:
    print("Nota inválida. Tente novamente")
  if num >0 and num <10:
    print("Parabéns!")
    num = 0

    
