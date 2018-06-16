import numpy as np
import matplotlib.pyplot as plt
from random import randint

def create_circle_label(x, y, r):
    
    output = []
    
    for i, j in zip(x, y):
        
        if i**2+j**2 <= r**2:
            output.append('#00ff00')
        else:
            output.append('#ff0ff0')    
    return output




x_min = -15
x_max = 15

x=np.arange(x_min,x_max)


y_min = -15
y_max = 15

y=np.arange(y_min,y_max)

X,Y = np.meshgrid(x,y)

print np.meshgrid(x,y)

print "Shape of X:", X.shape
print "Shape of Y:", Y.shape


X = X.flatten()
Y = Y.flatten()

plt.figure(figsize=(11, 11))
plt.scatter(X, Y)
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Cartesian 2D plane")
plt.show()





