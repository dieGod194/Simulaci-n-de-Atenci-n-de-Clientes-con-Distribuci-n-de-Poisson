import math
import random
import time

LAMBDA = 8

def simu():
    cajas = {1: [], 2: [], 3: [], 4: []}
    atendidos = {1: 0, 2: 0, 3: 0, 4: 0}
    registros_por_hora = {1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: []}
    
    for hora in range(8):
        arrivals = poisson_random(LAMBDA)
        
        for x in range(arrivals):
            valor = (x % 4) + 1
            formarse(cajas[valor], valor)
            
        for caja_num, caja in cajas.items():
            caja.sort(key=lambda x: sum([registro["Tiempo de atención"] for registro in registros_por_hora[hora + 1] if registro["Caja"] == caja_num]))
            
        for caja_num, caja in cajas.items():
            while caja:
                cliente_actual = caja.pop(0)
                caja_destino = min(cajas.keys(), key=lambda x: sum([registro["Tiempo de atención"] for registro in registros_por_hora[hora + 1] if registro["Caja"] == x]))
                tiempo_inicio = time.time()
                tiempo_atencion = random.randint(1, 10)
                # time.sleep(tiempo_atencion)  # Comentado para depuración
                tiempo_fin = time.time()
                tiempo_total_atencion = tiempo_fin - tiempo_inicio
                atendidos[caja_destino] += 1
                registro = {
                    "Cliente": atendidos[caja_destino],
                    "Caja": caja_destino,
                    "Hora": hora + 1,
                    "Tiempo de atención": tiempo_atencion
                }
                registros_por_hora[hora + 1].append(registro)
                
        print(f"En la hora {hora + 1}, llegaron {arrivals} clientes.")
    
    for hora, registros_hora in registros_por_hora.items():
        print(f"Registros para la hora {hora}:")
        registros_hora.sort(key=lambda x: x['Cliente'])  # Ordenar por orden de atención
        for registro in registros_hora:
            print(registro)
    
def poisson_random(lambda_val):
    k = 0
    p = 1.0
    exp_lambda = math.exp(-lambda_val)

    while p >= exp_lambda:
        k += 1
        p *= random.random()

    return k - 1
    
def formarse(cola, x):
    cola.append(x)
    
simu()