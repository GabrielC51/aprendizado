n = int(input("mande numeros "))

s = 0
for i in range(0, n, 3):
    print(i)
    s += i
print("a soma dos impares multiplos de 3 entre 1 e {} é:".format(n))
print(s)