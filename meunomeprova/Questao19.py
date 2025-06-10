numeros = [1,2,3]
print("Soma: ", sum(numeros))
soma_par=sum([n for n in numeros if n % 2 == 0])
print("Soma dos numeros pares:", soma_par)