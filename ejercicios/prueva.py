import random


def run():
    numero_aleatorio = random.randint(1, 1000)
    numero_elegido = int(input('Elige un numero de 1 a 100'))
    while numero_elegido != numero_aleatorio:
        if numero_elegido < numero_aleatorio:
            print('Busca un numero mas grande')
        else:
            print('Busca un numero mas pequeño')
    numero_elegido = int(input('Elige otro numero: '))
    print('Ganaste!!')


if __name__ == '__main__':
    run()
