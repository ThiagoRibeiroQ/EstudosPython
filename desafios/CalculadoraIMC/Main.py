def calcular_imc():

    print("--- Calculadora de Índice de Massa Corporal (IMC) ---")

  
    while True:
        try:
            peso = float(input("Digite seu peso em kg (ex: 75.5): "))
            if peso <= 0:
                print("Erro: O peso deve ser um valor positivo.")
                continue
            break
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")

    while True:
        try:
            altura = float(input("Digite sua altura em metros (ex: 1.80): "))
            if altura <= 0:
                print("Erro: A altura deve ser um valor positivo.")
                continue
            break
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")


    imc = peso / (altura ** 2)


    if imc < 18.5:
        classificacao = "Abaixo do peso"
    elif 18.5 <= imc < 25:
        classificacao = "Peso normal"
    elif 25 <= imc < 30:
        classificacao = "Sobrepeso"
    elif 30 <= imc < 35:
        classificacao = "Obesidade Grau I"
    elif 35 <= imc < 40:
        classificacao = "Obesidade Grau II"
    else: 
        classificacao = "Obesidade Grau III (Mórbida)"

    print("\n--- Resultado ---")
 
    print(f"Seu IMC é: {imc:.2f}")
    print(f"Classificação: {classificacao}")
    print("\nLembre-se: O IMC é um indicador. Consulte um profissional de saúde.")


if __name__ == "__main__":
    calcular_imc()