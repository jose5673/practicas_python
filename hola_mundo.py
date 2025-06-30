mensaje = "mi viaje comienza aquí y ahora"
mi_lista = ["hola", "mundo", 1, 2, 3]

print(mi_lista)
#.append(): Agrega un elemento al final de la lista.
mi_lista.append(6)
print(mi_lista)
#.insert(): Agrega un elemento en una posición específica de la lista.
mi_lista.insert(2, 7)
print(mi_lista)
#.remove(): Elimina un elemento de la lista.
mi_lista.remove(7)
print(mi_lista)
#.pop(): Elimina un elemento de la lista y lo devuelve.
mi_lista.pop(2)
print(mi_lista)
#.sort(): Ordena la lista.
mi_lista.sort()
print(mi_lista)
#.reverse(): Invierte la lista.
mi_lista.reverse()
print(mi_lista)
#.count(): Cuenta cuántas veces aparece un elemento en la lista.
print(mi_lista.count(2))
#.index(): Devuelve el índice de un elemento en la lista.
print(mi_lista.index(2))
#.extend(): Agrega una lista a otra lista.
mi_lista.extend(lista)
print(mi_lista)
#.clear(): Elimina todos los elementos de la lista.
mi_lista.clear()
print(mi_lista)
#.copy(): Crea una copia de la lista.
mi_lista = lista.copy()
print(mi_lista)
#.join(): Une todos los elementos de la lista con un string.
mensaje = " ".join(lista)
print(mensaje)
#.strip(): Elimina todos los espacios en blanco de ambos extremos.
print(mensaje.strip())
#.lstrip(): Elimina los espacios en blanco solo del principio (left strip).
print(mensaje.lstrip())
#.rstrip(): Elimina los espacios en blanco solo del final (right strip).
print(mensaje.rstrip())

print(mi_lista)
#.pop(): Elimina el último elemento de la lista.
mi_lista.pop()
print(mi_lista)
#.pop(posición): Elimina el elemento de la lista que se encuentre en la posición indicada.
mi_lista.pop(1)
print(mi_lista)
#.remove(elemento): Elimina el primer elemento de la lista que coincida con el elemento indicado.
mi_lista.remove("hola")
print(mi_lista)
#.reverse(): Invierte el orden de los elementos de la lista.
mi_lista.reverse()
print(mi_lista)
#.sort(): Ordena los elementos de la lista.
mi_lista.sort()
print(mi_lista)
#.sort(reverse=True): Ordena los elementos de la lista de forma descendente.
mi_lista.sort(reverse=True)
print(mi_lista)/listas.py
# Listas
mi_lista = ["hola", "mundo", 1, 2, 3]
#.append(elemento): Añade un elemento al final de la lista.
mi_lista.append("adios")
print(mi_lista)
#.insert(posición, elemento): Añade un elemento en la posición indicada.
mi_lista.insert(1, "hola")
print(mi_lista)
#.extend(lista): Añade los elementos de la lista indicada al final de la lista actual.
mi_lista.extend(["adios", "mundo"])
print(mi_lista)
#.count(elemento): Cuenta el número de veces que aparece el elemento indicado en la lista.
print(mi_lista.count("hola"))
#.index(elemento): Devuelve la posición del primer elemento de la lista que coincida con el elemento indicado.
print