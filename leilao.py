n = int(input())  

lance_maior = 0
maior_apostador = ""

for i in range(n):
    licitante = input().strip()  
    lance = int(input())  
    if lance > lance_maior:
        lance_maior = lance
        maior_apostador = licitante

print(maior_apostador)
print(lance_maior)

