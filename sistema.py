"""
Un comercio necesita registrar el importe final de tres compras.

En utils.py, completá estas funciones:

calcular_subtotal(precio, cantidad): retorna el precio multiplicado por la cantidad.
aplicar_descuento(subtotal): retorna el importe con un 10 % de descuento si el subtotal es igual
o mayor a $20.000. En caso contrario, retorna el subtotal sin cambios.
En systema.py, solicitá el precio unitario y la cantidad de cada compra. Invocá ambas funciones y agregá 
cada importe final a una lista llamada totales. Al terminar, mostrá la lista.
"""
import utils
print("Bienvenido al registro de importe final")
totales = []
for i in range(3):
    print(f"Cliente número {i + 1}")
    precio = float(input("Ingrese el precio unitario: "))
    cantidad = int(input("Ingrese la cantidad: "))
    subtotal = utils.calcular_subtotal(precio, cantidad)
    total = utils.aplicar_descuento(subtotal)
    totales.append(total)
    print(f"El importe final de la compra del cliente {i + 1} es: ${total}")

print("Importes finales registrados:")
for i, total in enumerate(totales, start=1):
    print(f"Cliente {i}: ${total}")