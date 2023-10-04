# verificar se a letra informada é vogal ou consoante

letra = input("Informe uma letra: ")

if letra.lower() in ('a', 'e', 'i', 'o', 'u'):
    print("A letra ", letra," é vogal")
elif letra in ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0'):
    print("Você não digitou uma letra!")
else:
    print("A letra", letra," é uma consoante!")