rendimento = int(input('Qual o rendimento da lata? '))
altura = int(input('Qual a altura da parede? '))
largura = int(input('Qual a largura da parede? '))

def calculo_tinta():
    area = altura * largura
    total = area/rendimento
    print(f'Você precisa de {total} latas de tinta')

calculo_tinta()

     