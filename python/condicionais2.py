valor = float(input('qual o valor da casa? '))
salario = float(input('qual o seu salario? '))
time = int(input('em quantas parcelas vc quer pagar? '))

parcela = valor/time
porcentagem = salario * 0.3
if parcela <= porcentagem:
    print("Sua casa vai sair por R${:.2f} por mês na quantidade de parcelas escolhidas".format(parcela))
else:
    print("infelizmente você não pode pagar :(")