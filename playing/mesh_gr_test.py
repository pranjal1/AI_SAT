import numpy as np
import matplotlib.pyplot as plt


x=np.arange(0,5)
y=np.arange(0,5)

print 'x is : '
print x
print ' '
print 'y is : '
print y

xv,yv = np.meshgrid(x,y)
print ' '
print 'xv is : '
print xv
print ' '
print 'yv is : '
print yv


xv= xv.flatten()
yv= yv.flatten()

print ' '
print 'after flatten'

print 'xv is : '
print xv

print ' '
print 'yv is : '
print yv

plt.figure(figsize=(11,11))
plt.scatter(xv,yv)
plt.show()
