# A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,... Faça um programa que gere a série até que o valor seja maior que 500.

fib = list(range(0,10))
i = 0
# print(fib[i])

while fib[i] < 500:
    if i < 2:
        fib[i] = 1
    else:
       fib[i] = fib[i-2] + fib[i-1]
    print(fib[i])
    i += 1
    

