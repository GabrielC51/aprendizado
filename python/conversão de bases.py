n = int(input("Mande o numero "))
b = input("qual a base que vc deseja? binario[1], octal [2] hexadecimal[3] ")

if b == '1':
    conv = bin(n)
elif b == '2' :
    conv = oct(n)
elif b == '3':
    conv = hex(n)
else:
    print('base invalida')
    end = 1/0
print("{} = {}".format(n, conv))