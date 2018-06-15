import random
import ast
print('####################')
print('#   Actividad 1b   #')
print('####################')
###### Definicion de funciones para el ejercicio
def dameNumero():    
    try:
        con = int(raw_input('Dame altura(0-32.000):'))                        
        return con            
    except ValueError:
        return 'false'

def numAleatorio():
    #return 1234
    return random.randint(1000,9999)

def comparaNum(num, aleatorio):
    num_str = list(str(num))
    aleatorio_str = list(str(aleatorio))
    aciertos = ""    
    for i in range(len(num_str)):
        if num_str[i] == aleatorio_str[i]:
            aciertos = aciertos + "x" 
        else:        
            aciertos = aciertos + num_str[i] 
    herido = 0
    for i in range(len(num_str)):
        for j in range(len(aleatorio_str)):
            if num_str[i] == aleatorio_str[j]: 
                herido = herido + 1
    return aciertos + " heridos " + str(herido)
    
################# Comienzo del ejercicio
seguir = 1
gravedad = 9.80665 # m/s2
troposferaPresion = (101325 - 22632) / 11000
troposferaDensidad = (1.2250 - 0.3639) / 11000
tropopausaPresion = (22632 - 5474.9) / (20000 - 11000)
tropopausaDensidad = (0.3629 - 0.0880) / (20000 - 11000)
estratosferaPresion = (5474.9 - 868.02) / (32000 - 20000)
estratosferaDensidad = (0.0880 - 0.0132) / (32000 - 20000)

while seguir == 1:
    num = dameNumero()
    if (num != 'false'):        
        if num >= 0 and num <= 32000:            
            if (num <= 11000):
                print("Estamos en la Troposfera")
                print("La Densidad para la altura de " + str(num) + " metros es: " + str( 1.2250 - (troposferaDensidad * num)) + " kg/m3")
                print("La Presion para la altura de " + str(num) + " metros es: " + str(101325 - (troposferaPresion * num)) + " Pa" + str(tropopausaPresion)+"  "+"")
            if (num > 11000 and num <= 20000):
                num = num - 11000
                print("Estamos en la Tropopausa")
                print("La Densidad para esa altura es: " + str(0.3639 - (tropopausaDensidad * num)) + " kg/m3")
                print("La Presion para esa altura es: " + str(22632 - (tropopausaPresion * num)) + " Pa")
            if (num > 20000 and num <= 32000):
                num = num - 20000
                print("Estamos en la Estratosfera")
                print("La Densidad para esa altura es: " + str(0.0880 - (estratosferaDensidad * num)) + " kg/m3")
                print("La Presion para esa altura es: " + str(5474.9 - (estratosferaPresion * num)) + " Pa")
        else:
            print("Numero debe estar comprendido entre 0 y 32.000")
    else:
        print("No es un numero")
