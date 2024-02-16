"""Módulo que contiene la función factorial"""


def factorial(num):
    """
   Función que devuelve el factorial de un número:


   Entrada:
   - entero: número entero mayor o igual a cero


   Salida:
   - entero: factorial de dicho número
   """

    if num == 1:
        return 1
    
    if not isinstance(num, int):
        raise TypeError("El argumento debe ser un entero")
   
    if num < 0:
        raise ValueError("El argumento debe ser un entero no negativo o cero")
    
    return num * factorial(num - 1) 
