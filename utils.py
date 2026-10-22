"""
Un comercio necesita registrar el importe final de tres compras.

En utils.py, completá estas funciones:

calcular_subtotal(precio, cantidad): retorna el precio multiplicado por la cantidad.
aplicar_descuento(subtotal): retorna el importe con un 10 % de descuento si el subtotal es igual
o mayor a $20.000. En caso contrario, retorna el subtotal sin cambios.
En systema.py, solicitá el precio unitario y la cantidad de cada compra. Invocá ambas funciones y agregá
cada importe final a una lista llamada totales. Al terminar, mostrá la lista.
"""

def calcular_subtotal(precio, cantidad):
    return precio * cantidad

def aplicar_descuento(subtotal):
    if subtotal >= 20000:
        return subtotal - (subtotal * 0.1)
    else:
        return subtotal
   