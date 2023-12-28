from z3 import *

# Definir variables
x0, y0, z0, t0, vx, vy, vz, t1, t2 = Reals('x0 y0 z0 t0 vx vy vz t1 t2')

# Definir ecuaciones
ecuaciones = [
    x0 + t0*vx == 150191335679733 + t0*239,
    y0 + t0*vy == 257950211885619 + t0*57,
    z0 + t0*vz == 282767497332049 + t0*42,
    x0 + t1*vx == 310843966440013 - t1*42,
    y0 + t1*vy == 307550528062309 - t1*26,
    z0 + t1*vz == 305058399233591 - t1*8,
    x0 + t2*vx == 240206072440513 + t2*44,
    y0 + t2*vy == 257955942583195 + t2*13,
    z0 + t2*vz == 339853739319015 + t2*18
]

# Crear solver
solver = Solver()

# Agregar ecuaciones al solver
solver.add(ecuaciones)

# Verificar si el sistema de ecuaciones es satisfactible
if solver.check() == sat:
    # Obtener el modelo
    modelo = solver.model()

    # Obtener los valores de las variables
    valor_x0 = modelo[x0].as_decimal(9)
    valor_y0 = modelo[y0].as_decimal(9)
    valor_z0 = modelo[z0].as_decimal(9)
    valor_t0 = modelo[t0].as_decimal(9)
    valor_vx = modelo[vx].as_decimal(9)
    valor_vy = modelo[vy].as_decimal(9)
    valor_vz = modelo[vz].as_decimal(9)
    valor_t1 = modelo[t1].as_decimal(9)
    valor_t2 = modelo[t2].as_decimal(9)

    print(f"Solución encontrada: x0 = {valor_x0}, y0 = {valor_y0}, z0 = {valor_z0}, "
          f"t0 = {valor_t0}, vx = {valor_vx}, vy = {valor_vy}, vz = {valor_vz}, "
          f"t1 = {valor_t1}, t2 = {valor_t2}")
else:
    print("No se encontró solución para el sistema de ecuaciones.")
