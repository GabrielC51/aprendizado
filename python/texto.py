nomec = input("envie o seu nome completo ")
print(nomec.lower())
print(nomec.upper())
print(len(nomec) - nomec.count(' '))
nomesep = nomec.split()
print(len(nomesep[0]))

n = input("escreva um numero de 0 a 9999 ")

if (int(n) < 10) :
    n = "000" + n
elif (int(n) <100) :
    n = "00" + n
elif (int(n) <1000) :
    n = "0" + n

print("unidade: {} \ndezena: {} \ncentena: {} \nmilhar: {}" .format(n[3],n[2],n[1],n[0]))

cidade = input("qual o nome da sua cidade? ") 
print('santo' in cidade.lower())