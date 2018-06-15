from pylab import *
x=[0.2,1.3,2.1,2.9,3.3]
y=[3.3,3.9,4.8,5.5,6.9]

(m,b)=polyfit(x,y,1)
print(b)
print(m)

yp=polyval([m,b],x)

plot(x,yp)
scatter(x,y)
grid(True)
xlabel('x')
ylabel('y')
show()