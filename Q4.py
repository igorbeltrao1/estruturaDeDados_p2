ano =  int(input("Digite o ano que desejas consutar: "))

div = ano % 4

if div == 0:
    print("O ano é bissexto")
else:
    print("O ano não é bissexto")