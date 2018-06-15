import random
import ast
print('####################')
print('#   Actividad 1    #')
print('####################')
###### Definicion de funciones para el ejercicio
def dameNumero():    
    try:
        con = int(raw_input('Dame numero de 4 cifras:'))                
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
aleatorio = numAleatorio() 
while seguir == 1:
    num = dameNumero()
    if (num != 'false'):        
        if num == aleatorio:
            seguir = 0
            print("*******************")
            print("*   CONSEGUIDO    *")
            print("*******************")
        else:
            aciertos = comparaNum(num, aleatorio)    
            print("x=muertos -=heridos")            
            print(aciertos)
            print(num)

