


def votar_amigos(n_amigos):
    votos_cine = 0
    votos_fiesta = 0
    
    for i in range(n_amigos):
        while True:
            voto = input(f"Amigo {i+1}, ¿prefieres 'cine' o 'fiesta'?: ").strip().lower()
            if voto in ('cine', 'fiesta'):
                if voto == 'cine':
                    votos_cine += 1
                else:
                    votos_fiesta += 1
                break
            else:
                print("Entrada no válida. Por favor, introduce 'cine' o 'fiesta'.")
    
    return votos_cine, votos_fiesta

def calcular_porcentaje(votos, total_votos):
    return (votos / total_votos) * 100

def decidir_actividad(votos_cine, votos_fiesta):
    total_votos = votos_cine + votos_fiesta
    porcentaje_cine = calcular_porcentaje(votos_cine, total_votos)
    porcentaje_fiesta = calcular_porcentaje(votos_fiesta, total_votos)
    
    if porcentaje_cine > porcentaje_fiesta:
        actividad_elegida = 'CINE'
    elif porcentaje_fiesta > porcentaje_cine:
        actividad_elegida = 'FIESTA'
    else:
        actividad_elegida = 'CINE'  # En caso de empate se elige 'CINE'
    
    return porcentaje_cine, porcentaje_fiesta, actividad_elegida

def calcular_vaquita(total_dinero, n_amigos):
    return total_dinero / n_amigos

# Programa principal
while True:
    try:
        n_amigos = int(input("Indique la cantidad de participantes de los amigos: "))
        if n_amigos > 0:
            break
        else:
            print("La cantidad de participantes debe ser mayor a cero.")
    except ValueError:
        print("Entrada no válida. Por favor, introduce un número entero mayor a cero.")

# Realizar votación
votos_cine, votos_fiesta = votar_amigos(n_amigos)

# Calcular porcentajes y decidir actividad
porcentaje_cine, porcentaje_fiesta, actividad_elegida = decidir_actividad(votos_cine, votos_fiesta)

# Mostrar resultados de la votación
print("Porcentaje de votos para CINE: {:.2f}%".format(porcentaje_cine))
print("Porcentaje de votos para FIESTA")