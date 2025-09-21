funcionarios = ['Thiago', 'Pedro', 'Matheus', 'Álvaro']
turno_dia = ['Thiago', 'Pedro']
turno_noite = ['Matheus', 'Álvaro']
tem_carro = ['Pedro', 'Álvaro']


lista1 = set(tem_carro).intersection(turno_noite)
print(lista1)

lista2 = set(tem_carro).intersection(turno_dia)
print(lista2)

lista3 = set(funcionarios).difference(tem_carro)
print(lista3)