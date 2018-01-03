from PIL import Image
import numpy as np
from matplotlib import pyplot as plt
import os
import math
import sys
path = '/Users/rgirish28/Documents/Strip JPEGs/'


def entropy(signal):
    lensig=signal.size
    symset=list(set(signal))
    numsym=len(symset)
    propab=[np.size(signal[signal==i])/(1.0*lensig) for i in symset]
    ent=np.sum([p*np.log2(1.0/p) for p in propab])
    return ent

colorIm1=Image.open(os.path.join(path,sys.argv[1]))
greyIm=colorIm1.convert('L')
colorIm=np.array(colorIm1)
greyIm=np.array(greyIm)

N=5
S=greyIm.shape
E=np.array(greyIm)
for row in range(S[0]):
    for col in range(S[1]):    
       
        Lx=np.max([0,col-N])
        Ux=np.min([S[1],col+N])
        Ly=np.max([0,row-N])
        Uy=np.min([S[0],row+N])
        region=greyIm[Ly:Uy,Lx:Ux].flatten()
        E[row,col]=entropy(region)

plt.subplot(1,3,1)
plt.imshow(colorIm)

plt.subplot(1,3,2)
plt.imshow(greyIm, cmap=plt.cm.gray)

plt.subplot(1,3,3)
plt.imshow(E, cmap=plt.cm.jet)
plt.xlabel('Entropy in '+str(2*N)+'x' +str(2*N)+' neighbourhood')
plt.colorbar()

plt.show()



rgbHistogram = colorIm1.histogram()

print 'Snannon Entropy for Red, Green, Blue:'
for rgb in range(3):
        
    totalPixels = sum(rgbHistogram[rgb * 256 : (rgb + 1) * 256])
    
    ent = 0.0
    
    for col in range(rgb * 256, (rgb + 1) * 256):
    
        freq = float(rgbHistogram[col]) / totalPixels
        
        if freq > 0:
        
            ent = ent + freq * math.log(freq, 2)
            
    ent = -ent
            
    print ent


hist = colorIm1.histogram()
hist_size = sum(hist)
hist = [float(h) / hist_size for h in hist]
print 'Image Entropy:'
print -sum(p * math.log(p, 2) for p in hist if p != 0)
