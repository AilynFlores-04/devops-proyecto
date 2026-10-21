def sumar(a, b):
    return a + b


def restar(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    if b == 0:
        raise ZeroDivisionError("No se puede dividir entre cero")
    return a / b

def funcion_nueva_con_bug():
    # Este bug haría fallar la aplicación en producción
    return 1 / 0

def funcion_nueva_con_bug():
    return 1 / 0
