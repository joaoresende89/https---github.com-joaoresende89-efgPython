# A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de gerar a série até o n−ésimo termo.

num = int(input("Informe quantos termos você quer ver da sequincia Fibonacci: "))

if num < 1:
    exit()

fib = list(range(num))

for i in range(0,num):
    if i < 2:
        fib[i] = 1
    else:
       fib[i] = fib[i-2] + fib[i-1]
    print(fib[i])

