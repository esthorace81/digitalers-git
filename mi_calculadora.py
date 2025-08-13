__version__ = "1.0.0"

"""
Un simple programa para realizar cálculos básicos
"""


def sumar(a, b):
    return a + b


def restar(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


print("¡Bienvenido a mi calculadora!")

resultado_suma = sumar(100, 50)
print(f"El resultado de la suma es: {resultado_suma}")

resultado_resta = restar(10, 5)
print(f"El resultado de la resta es: {resultado_resta}")

resultado_multiplicacion = multiplicar(10, 5)
print(f"El resultado de la multiplicación es: {resultado_multiplicacion}")
