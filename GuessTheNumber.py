import random

intentosRealizados = 0

print('Hola!!! ¿Como te llamas?')
nombreJugador = input()

numero = random.randint(1, 20)
print('Bueno, ' + nombreJugador + ', estoy pensando en un número entre 1 y 20.')

while intentosRealizados < 6:
    print('Intenta adivinar.')
    estimacion = int(input())

    intentosRealizados = intentosRealizados + 1

    if estimacion < numero:
        print('Tu estimación es muy baja.')

    if estimacion > numero:
        print('Tu estimación es muy alta.')

    if estimacion == numero:
        break

if estimacion == numero:
    intentosRealizados = str(intentosRealizados)
    print('¡Buen Trabajo, ' + nombreJugador + '! ¡Has adivinado mi numero en ' + intentosRealizados + ' intentos!')

if estimacion != numero:
    numero = str(numero)
    print('Pues no. El numero que estaba pensando era ' + numero)
