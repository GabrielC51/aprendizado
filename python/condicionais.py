l1 = int(input("manda lado 1, 2 e 3"))
l2 = int(input())
l3 = int(input())

if l1 < l2 + l3 and l2 < l3 + l1 and l3 < l1 + l2:
    print("é um triangulo plausivel")
else:
    print("não é plausivel")