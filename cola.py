import math
import random

LAMBDA = 20

def simu():
    caja1=[]
    caja2=[]
    caja3=[]
    caja4=[]
    atendidos1=0
    atendidos2=0
    atendidos3=0
    atendidos4=0
    registro1=[]
    registro2=[]
    registro3=[]
    registro4=[]
    
    for hora in range(8): # Simulamos 8 horas
    
        arrivals = poisson_random(LAMBDA)
        for x in range(0,arrivals): #Dividimos a los clientes entre las 4 cajas
            valor = (x % 4) + 1
            if valor==1:
                formarse(caja1, valor)
                dic1={}
                for y in range(len(caja1)):
                    numran = random.randint(1, 10)
                    clave = f"El Cliente {len(caja1)} de la caja 1 en la hora {hora+1} fue atendido en"
                    dic1[clave] = f"{numran} segundos"
                    atendidos1+=1 #poner esto despues de implementar el atender
            elif valor==2:
                formarse(caja2, valor)
                dic2={}
                for y in range(len(caja1)):
                    numran = random.randint(1, 10)
                    clave = f"El Cliente {len(caja1)} de la caja 2 en la hora {hora+1} fue atendido en"
                    dic2[clave] = f"{numran} segundos"
                atendidos2+=1
            elif valor==3:
                formarse(caja3, valor)
                dic3={}
                for y in range(len(caja1)):
                    numran = random.randint(1, 10)
                    clave = f"El Cliente {len(caja1)} de la caja 3 en la hora {hora+1} fue atendido en"
                    dic3[clave] = f"{numran} segundos"
                atendidos3+=1
            elif valor==4:
                formarse(caja4, valor)
                dic4={}
                for y in range(len(caja1)):
                    numran = random.randint(1, 10)
                    clave = f"El Cliente {len(caja1)} de la caja 4 en la hora {hora+1} fue atendido en"
                    dic4[clave] = f"{numran} segundos"
                atendidos4+=1
        print(f"En la hora {hora + 1}, llegaron {arrivals} clientes.")
        registro1.append(dic1)
        registro2.append(dic2)
        registro3.append(dic3)
        registro4.append(dic4)
        caja1.clear() #impiamos todas las cajas para la siguiente hora
        caja2.clear()
        caja3.clear()
        caja4.clear()
    
    print("caja 1 atendio:", atendidos1,"caja 2 atendio:", atendidos2,"caja 3 atendio:", atendidos3,"caja 4 atendio:", atendidos4)#asi sacamos cuantos clientes se atendieron en cada caja
    print(registro1)
    print(registro2)
    print(registro3)
    print(registro4)


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
