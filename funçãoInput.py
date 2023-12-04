"""
input():

Função: A função input() é usada para receber dados de entrada do usuário.
Uso: Quando você chama input(), o programa aguarda a entrada do usuário. O
usuário pode digitar qualquer coisa e pressionar Enter. O valor
inserido é tratado como uma string (texto) e pode ser
atribuído a uma variável para uso posterior no programa.

print():

Função: A função print() é usada para exibir informações na saída padrão
(normalmente o console).
Uso: Quando você chama print(), o valor passado como argumento é exibido
no console. Pode ser uma string, uma variável, ou uma expressão.

Em resumo, input() é usado para obter dados de entrada do usuário, enquanto print()
é usado para exibir informações na saída.
Ambas são funções fundamentais para interagir
com o usuário e mostrar resultados em um programa Python.
"""

nome = "Ricardo"
idade = 24
peso = 64.82

print(f"Meu nome é {nome}\nMinha idade é {idade}\nMeu peso {peso}kg")

# Forma utilizando a função INPUT()

print("\n")

nome = str(input("Favor inserir nome do usuario: "))
idade = int(input("Favor inserir idade do usuario: "))
peso = float(input("Favor inserir o peso do usuario: "))

"""
A diferença principal é que o input() retorna uma string (sequência de caracteres) e, em alguns casos, 
você pode querer explicitamente converter esse valor para outro tipo de dado, como no exemplo em que usamos 
str() para garantir que o valor inserido seja tratado como uma string.

No entanto, em muitos casos, essa conversão pode não ser necessária. Se você deseja que 
o valor inserido seja tratado como uma string, pode omitir a conversão e simplesmente usar:

    nome = input ("Favor inserir nome do usuario: ")

"""

print("\n")

print(f"Meu nome é {nome}\nMinha idade é {idade}\nMeu peso {peso}kg")


