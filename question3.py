import json

with open("dados.json", "r") as file:
    dados = json.load(file)

menor_faturamento = float("inf")
maior_faturamento = 0
total_faturamento = 0
dias_acima_da_media = 0

for dia in dados:
    valor = dia["valor"]
    if valor > maior_faturamento:
        maior_faturamento = valor
    if valor < menor_faturamento and valor != 0:
        menor_faturamento = valor
    total_faturamento += valor

media_faturamento = total_faturamento / len(dados)

for dia in dados:
    if dia["valor"] > media_faturamento and dia["valor"] != 0:
        dias_acima_da_media += 1

print(f"Menor faturamento diário: R$ {menor_faturamento:.2f}")
print(f"Maior faturamento diário: R$ {maior_faturamento:.2f}")
print(f"Dias acima da média: {dias_acima_da_media}")