from collections import deque

# Crear una cola con deque para almacenar strings
mi_cola = deque()
mi_cola.append("ppp")
nuevos_strings = ["abc", "def", "ghi", "jkl"]
mi_cola.extend(["xxx"])
mi_cola.extend(nuevos_strings)
print("Cola:", mi_cola)