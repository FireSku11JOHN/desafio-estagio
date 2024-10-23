# Sequencia de Fibonacci

def fibonacci(numero):
    n1, n2 = 0, 1
    while n1 <= numero:
        # Compara se o número atual da sequência é o mesmo do input do usuario
        if n1 == numero:
            return True
        n1, n2 = n2, n1 + n2 #Soma do proximo número da sequência
    return False

# Input
numero = int(input("Digite um número: "))

if fibonacci(numero):
    print(f"O número {numero} está na sequência de Fibonacci.")
else:
    print(f"O número {numero} não está na sequência de Fibonacci.")

