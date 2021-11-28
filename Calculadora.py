valor= float(input('Qual o valor da casa que deseja comprar? R$'))
salario= float(input('Quanto você ganha? R$'))
prestacoes= int(input('Em quantas parcelas deseja quitar a casa?'))
c1= (valor / prestacoes)
c2= 0.3 * salario
if c1 > c2:
    print('Sinto muito, seu empréstimo foi negado!')
else:
    print('Vamos iniciar sua compra!')
