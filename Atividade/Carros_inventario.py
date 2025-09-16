import datetime


class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

        Carro.total_carros += 1
        print(f"Novo carro adicionado ao inventário: {self.marca} {self.modelo}")

    def carro_informacoes():
        print(f'Marca: {self.marca} | Modelo: {self.modelo} | Ano: {self.ano}')

     @staticmethod

