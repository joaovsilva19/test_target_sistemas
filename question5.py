texto = (input("Digite o texto que deseja inverter: "))

texto_invertido = ""

for i in range(len(texto)-1, -1, -1):
    texto_invertido += texto[i]

print("Texto invertido:", texto_invertido)