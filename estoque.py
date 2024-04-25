M, N = map(int, input().split())
stock = [list(map(int, input().split())) for _ in range(M)]
P = int(input())
vendido = 0

for _ in range(P):
    I, J = map(int, input().split())
    if stock[I-1][J-1] > 0:
        stock[I-1][J-1] -= 1
        vendido += 1

print(vendido)
