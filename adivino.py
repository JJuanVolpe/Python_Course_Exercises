## Adivina adivinador....
import random

numero_aleatorio = random.randrange(100)


exist_winner = False
print("Tenés 5 intentos para adivinar un numero entre 0 y 99")
actual_choice = 1

max_choice = 5
while actual_choice <= max_choice and not exist_winner:
    numeroIngresado = int(input('Ingresa tu número: '))
    if numeroIngresado == numero_aleatorio:
        print('Ganaste! y necesitaste {} intentos!!!'.format(actual_choice))
        exist_winner = True
    else:
        print('Mmmm ... No.. ese número no es... Seguí intentando.')
        actual_choice += 1
if not exist_winner:
    print('\n Perdiste :(\n El número era: {}'.format(numero_aleatorio))
