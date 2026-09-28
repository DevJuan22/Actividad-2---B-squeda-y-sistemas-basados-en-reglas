conexiones = {
    "Portal Norte": ["Calle 100"],
    "Calle 100": ["Portal Norte", "Calle 76"],
    "Calle 76": ["Calle 100", "Héroes"],
    "Héroes": ["Calle 76", "Calle 72"],
    "Calle 72": ["Héroes", "Flores"],
    "Flores": ["Calle 72", "Calle 63"],
    "Calle 63": ["Flores", "Salitre - El Greco"],
    "Salitre - El Greco": ["Calle 63", "Portal Américas"],
    "Portal Américas": ["Salitre - El Greco"]
}


from collections import deque


def encontrar_ruta(origen, destino):
    cola = deque([[origen]])
    visitadas = set()

    while cola:
        ruta = cola.popleft()
        estacion_actual = ruta[-1]

        if estacion_actual == destino:
            return ruta

        if estacion_actual in visitadas:
            continue

        visitadas.add(estacion_actual)

        for siguiente in conexiones.get(estacion_actual, []):
            nueva_ruta = ruta + [siguiente]
            cola.append(nueva_ruta)

    return None

print("==========================================")
print("   SISTEMA INTELIGENTE DE RUTAS")
print("==========================================")

print("\nEstaciones disponibles:")

for estacion in conexiones:
    print("-", estacion)

print("\n------------------------------------------")

origen = input("Ingrese la estación de origen: ")
destino = input("Ingrese la estación de destino: ")

if origen not in conexiones:
    print("\nError: la estación de origen no existe.")

elif destino not in conexiones:
    print("\nError: la estación de destino no existe.")

elif origen == destino:
    print("\nEl origen y el destino son iguales.")

else:
    ruta = encontrar_ruta(origen, destino)

    if ruta:
        print("\nRuta encontrada:")
        print(" → ".join(ruta))

        print(f"\nNúmero de estaciones: {len(ruta)}")

    else:
        print("\nNo se encontró una ruta entre las estaciones.")