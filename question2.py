def fibonacci(n):
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
    if b == n:
        print("O número", n, "pertence à sequência de Fibonacci.")
    else:
        print("O número", n, "não pertence à sequência de Fibonacci.")

valor = int(input("Digite um número inteiro: "))
fibonacci(valor)