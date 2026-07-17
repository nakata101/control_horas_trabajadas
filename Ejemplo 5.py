# -------------------------------------------------------
# Problema 5
# Autor: Javier Silva
# Curso: Fundamentos de Programación
# -------------------------------------------------------

# Matriz con el nombre del recurso y las horas trabajadas
# de lunes a viernes.
recursos = [
    ["Juan", 8, 8, 9, 8, 8],
    ["María", 8, 8, 8, 8, 8],
    ["Pedro", 10, 9, 9, 8, 9],
    ["Laura", 7, 8, 7, 8, 8]
]

# Función que calcula el total de horas y la clasificación.
def calcular_total_horas(horas):
    total = sum(horas)

    if total > 40:
        clasificacion = "Sobretiempo"
    else:
        clasificacion = "Horario Estándar"

    return total, clasificacion

print("=" * 60)
print("      REPORTE DE HORAS TRABAJADAS")
print("=" * 60)

# Recorrer la matriz
for recurso in recursos:
    nombre = recurso[0]
    horas = recurso[1:]

    total, clasificacion = calcular_total_horas(horas)

    print(f"\nRecurso       : {nombre}")
    print(f"Total horas   : {total}")
    print(f"Clasificación : {clasificacion}")

print("\nProceso finalizado correctamente.")
