# Receba 10 valores e exiba a soma de todos eles
x = [int(input(f"Digite o valor numero {i}: ")) for i in range(0,10)]

soma = 0
for i in x:
    soma += i
print(soma)