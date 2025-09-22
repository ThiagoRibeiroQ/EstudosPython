class Termostato:
    def __init__(self, temperatura_atual):
        self._temperatura_min = 16.0
        self._temperatura_max = 30.0
        
        self.temperatura_atual = float(temperatura_atual)
        self.temperatura_desejada = float(temperatura_atual)
        
        print("Termostato iniciado.")

    def __str__(self):
        return (f"Status: Atual: {self.temperatura_atual:.1f}°C | "
                f"Desejada: {self.temperatura_desejada:.1f}°C")

    def aumentar_temperatura(self):
        if self.temperatura_desejada < self._temperatura_max:
            self.temperatura_desejada += 1
            print(f"Temperatura desejada aumentada para {self.temperatura_desejada:.1f}°C.")
        else:
            print(f"AVISO: Temperatura máxima de {self._temperatura_max:.1f}°C já foi atingida.")

    def diminuir_temperatura(self):
        if self.temperatura_desejada > self._temperatura_min:
            self.temperatura_desejada -= 1
            print(f"Temperatura desejada diminuída para {self.temperatura_desejada:.1f}°C.")
        else:
            print(f"AVISO: Temperatura mínima de {self._temperatura_min:.1f}°C já foi atingida.")

    def ajustar_temperatura(self, nova_temp):
        if self._temperatura_min <= nova_temp <= self._temperatura_max:
            self.temperatura_desejada = float(nova_temp)
            print(f"Temperatura desejada ajustada para {self.temperatura_desejada:.1f}°C.")
        else:
            print(f"ERRO: Valor inválido. A temperatura deve estar entre "
                  f"{self._temperatura_min:.1f}°C e {self._temperatura_max:.1f}°C.")

    def verificar_status_operacional(self):
        if self.temperatura_atual > self.temperatura_desejada:
            return "Resfriando... ❄️"
        elif self.temperatura_atual < self.temperatura_desejada:
            return "Aquecendo... 🔥"
        else:
            return "Temperatura estável. ✅"
 
if __name__ == "__main__":
    meu_termostato = Termostato(25)
    print(meu_termostato)
    print(f"Ação: {meu_termostato.verificar_status_operacional()}")
    print("-" * 30)

    print("Diminuindo a temperatura desejada...")
    meu_termostato.diminuir_temperatura()
    meu_termostato.diminuir_temperatura()
    print(meu_termostato)
    print(f"Ação: {meu_termostato.verificar_status_operacional()}")
    print("-" * 30)


    print("Tentando ajustar para uma temperatura muito alta...")
    meu_termostato.ajustar_temperatura(35)
    print(meu_termostato)
    print("-" * 30)
    

    print("Ajustando para uma temperatura válida...")
    meu_termostato.ajustar_temperatura(28)
    print(meu_termostato)
    print(f"Ação: {meu_termostato.verificar_status_operacional()}")
    print("-" * 30)

    print("Tentando diminuir a temperatura até o limite mínimo...")
    for _ in range(15):
        meu_termostato.diminuir_temperatura()
    print(meu_termostato)