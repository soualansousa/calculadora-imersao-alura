# --- Funções das Operações Matemáticas ---

def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    # Verificação de segurança para evitar divisão por zero
    if b == 0:
        return "Erro: Não é possível dividir por zero!"
    return a / b


# --- Função Principal ---

def calculadora():
    while True:
        print("\n=== CALCULADORA SIMPLES ===")
        print("1. Soma (+)")
        print("2. Subtração (-)")
        print("3. Multiplicação (*)")
        print("4. Divisão (/)")
        print("0. Sair")
        
        opcao = input("\nEscolha a operação desejada (0-4): ")

        # Condição de parada do programa
        if opcao == "0":
            print("Encerrando a calculadora. Até logo!")
            break

        # Valida se a opção escolhida existe
        if opcao in ["1", "2", "3", "4"]:
            try:
                num1 = float(input("Digite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))
            except ValueError:
                print("Erro: Entrada inválida. Por favor, digite apenas números.")
                continue

            # Executa a operação correspondente
            if opcao == "1":
                print(f"Resultado: {num1} + {num2} = {somar(num1, num2)}")
            elif opcao == "2":
                print(f"Resultado: {num1} - {num2} = {subtrair(num1, num2)}")
            elif opcao == "3":
                print(f"Resultado: {num1} * {num2} = {multiplicar(num1, num2)}")
            elif opcao == "4":
                print(f"Resultado: {num1} / {num2} = {dividir(num1, num2)}")
        else:
            print("Opção inválida! Escolha um número entre 0 e 4.")


# Ponto de entrada do programa
if __name__ == "__main__":
    calculadora()