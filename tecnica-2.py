# Contador de letras

def contador_letra(palavra):
    palavra = palavra.lower()

    qnt_letra = palavra.count('a')

    if qnt_letra > 0:
        print(f"A letra 'a' aparece {qnt_letra} vez(es) na palavra '{palavra}'.")
    
    else:
        print(f"A letra 'a' não foi encontrada na palavra '{palavra}'.")

palavra = input(str('Digite uma palavra: '))
contador_letra(palavra)
