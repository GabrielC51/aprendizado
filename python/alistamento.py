from datetime import date
nasc = int(input('quando vc nasceu? (ano) '))
data = date.today()
#print(data)
ano = data.year
#print(ano)
idade = ano - nasc
#print(idade)
if idade < 18:
    print('não chegou o tempo')
elif idade == 18:
    print('é agora')
else:
    print('ja passou da hora')