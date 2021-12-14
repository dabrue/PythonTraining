#!/usr/bin/python
import numpy
import scipy.fftpack as fftp
import math
import matplotlib.pyplot as plt

# Generate a 1D distribution
xmax=10.0
xmin=-xmax
N=10001

x = numpy.linspace(xmin,xmax,N)
y = numpy.zeros_like(x)

#for i in range(len(x)):
#    y[i]=math.exp(-(x[i]**2))

for i in range(len(x)):
    if (x[i] >= -3.0 and x[i] <= 3.0):
        y[i]=2.0
    if (x[i] >= -0.5 and x[i] <= 0.5):
        y[i]=4.0

t=fftp.fft(y)
rfftx=[]
ifftx=[]
for i in range(len(t)):
    rfftx.append(t[i].real)
    ifftx.append(t[i].imag)

# Reorder in terms of frequency
mid=(N-1)/2+1
a=list(rfftx[:mid])
b=list(rfftx[mid:])
a.reverse()
b.reverse()
rfreq=a+b
a=list(ifftx[:mid])
b=list(ifftx[mid:])
a.reverse()
b.reverse()
ifreq=a+b
mfreq=numpy.zeros_like(x)
for i in range(len(mfreq)):
    mfreq[i]=(rfreq[i]**2+ifreq[i]**2)/(2.0*math.pi)


fig=plt.figure()
ax0=fig.add_subplot(2,1,1)
plt.plot(x,y,"k-")
ax1=fig.add_subplot(2,1,2)
plt.plot(x,mfreq,"r-")
plt.show()

otf=open("out","w")
for i in range(len(x)):
    otf.write(str(x[i]).rjust(10)+str(y[i]).rjust(20)+str(rfftx[i]).rjust(20)+str(ifftx[i]).rjust(20)+"\n")
otf.close()


