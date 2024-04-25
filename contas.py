V = int(input())
A = int(input())
F = int(input())
P = int(input())


total = A + F + P

if total <= V:
    print(3)
else:

    if A + F <= V or A + P <= V or F + P <= V:
        print(2)
    else:

        if A <= V or F <= V or P <= V:
            print(1)
        else:

            print(0)

