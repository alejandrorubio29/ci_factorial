

def factorial(num):
    
    # El factorial d'1 és 1 -> refactorizacion
    if num == 1:
        return 1
    
    # Llança una excepció TypeError en no rebre un enter -> refactorizacion
    if not isinstance(num, int):
        raise TypeError("El argumento debe ser un entero")
    
    # Llança una excepció ValueError en rebre un enter negatiu -> refactorizacion
    if num < 0:
        raise ValueError("El argumento debe ser un entero no negativo o cero")
    # El factorial de 5 és 120 -> refactorizacion. Es la formula general del factorial
    else:
        return num * factorial(num - 1) # Es una funcion recursiva, se llama a si misma
