from pylab import * 
import random
### funcion para hayar la linea de regresion
def slope_intercept(x_val, y_val):
    x = np.array(x_val)
    y = np.array(y_val)
    m = ( ( np.mean(x) * np.mean(y) - np.mean(x * y))/
         ((np.mean(x) * np.mean(x))- np.mean(x*x)))
    m = round(m, 2)
    b = (np.mean(y) - np.mean(x) * m)
    b = round(b, 2)
    
    return m,b
#### vector X 11 números reales espaciados uniformemente entre 0 y 20
X = [None] * 11
for i in range(11):
    X[i]= random.uniform(0, 20)


#### Generar un vector Y=5+2X+Z, Z siendo un numero aleatorio entre -1 y 1 distinto para cada uno de los 11 puntos
Y = [None] * 11
Z = [None] * 11
for i in range(11):
    Z[i] = random.uniform(-1, 1)
    Y[i] = 5 + (2*X[i]) + Z[i]
#      8.29175995815   22.1569705806   0.573450664285
print("      X                Y               Z")
for i in range(11):
    print(str(X[i]) + "   " + str(Y[i]) + "   " + str(Z[i]))

##### Calcular los coeficientes de la recta de regresión que mejor se adapta a los puntos (X, Y) generados.
reg_line = slope_intercept(X, Y)
print("Linea de regresion = " + str(reg_line))

# Dibujar los puntos (X,Y) y la recta de regresión en la misma gráfica
    # polyfit es para hayar linea de regresion para la gráfica
    #(m,b)=polyfit(X,Y,1)
(m, b) = (reg_line)
yp=polyval([m,b],X)
plot(X,yp)
scatter(X, Y, color="red")
grid(True)
xlabel('x')
ylabel('y')
show()

