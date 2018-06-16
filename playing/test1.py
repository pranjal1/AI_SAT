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

print "Shape of X:", X.shape
print "Shape of Y:", Y.shape


X = X.flatten()
Y = Y.flatten()

plt.figure(figsize=(11, 11))
plt.scatter(X, Y)
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Cartesian 2D plane")
plt.savefig('cart_plot.png')



circle_label = create_circle_label(x=X, y=Y, r=8)

plt.figure(figsize=(11, 11))
plt.scatter(X, Y, c=circle_label) #https://matplotlib.org/gallery/shapes_and_collections/scatter.html
plt.xlabel("x coordinates")
plt.ylabel("y coordinates")
plt.title("Circular area labels")
plt.savefig('circle.png')





#Let's generate some random X, Y data X = [ [frst group],[second group] ...]
X = [ [randint(0,50) for i in range(0,5)] for i in range(0,24)]
Y = [ [randint(0,50) for i in range(0,5)] for i in range(0,24)]

print X
print Y

labels = range(1,len(X)+1)

fig = plt.figure(figsize=(11, 11))
ax = fig.add_subplot(111)
for x,y,lab in zip(X,Y,labels):
        ax.scatter(x,y,label=lab)



colormap = plt.cm.gist_ncar #nipy_spectral, Set1,Paired  
colorst = [colormap(i) for i in np.linspace(0, 0.9,len(ax.collections))]       
for t,j1 in enumerate(ax.collections):
    j1.set_color(colorst[t])


ax.legend(fontsize='small')

plt.savefig('fig.png')
