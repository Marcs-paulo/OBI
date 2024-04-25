S, T = map(int, input().split())
tuneis = {}
for i in range(T):
    X, Y = map(int, input().split())
    tuneis[(X, Y)] = True
    tuneis[(Y, X)] = True
X

P = int(input())
possiveis_sugestões = 0
for i in range(P):
    sequencia = list(map(int, input().split()))[1:]
    
    for j in range(len(sequencia) - 1):
        if (sequencia[j], sequencia[j+1]) not in tuneis:
            break
    else:
       
        possiveis_sugestões += 1

print(possiveis_sugestões)
