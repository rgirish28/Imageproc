from PIL import Image
import numpy as np
from matplotlib import pyplot as plt
import os
from matplotlib.legend_handler import HandlerLine2D
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

def image_entropy(img):

    hist = img.histogram()
    hist_size = sum(hist)
    hist = [float(h) / hist_size for h in hist]
    
    return -sum(p * math.log(p, 2) for p in hist if p != 0)

random = [0.0,0.1,0.3,0.6,1,"Strip"]


for i in range(1,7):

    colorIm1=Image.open(os.path.join(path,sys.argv[i]))
    greyIm1=colorIm1.convert('L')
    colorIm=np.array(colorIm1)
    greyIm=np.array(greyIm1)

    N=5
    S=greyIm.shape

    E = np.zeros(S[0]-2*N)


    for row in range(S[0]-2*N):    
       
        Ly=np.max([0,row-N])
        Uy=np.min([S[0],row+N])
        region=greyIm1.crop( (0,Ly, S[1],Uy) )
        E[row]=image_entropy(region)

    #plt.figure(1)
    #plt.subplot(1,2,1)
    #plt.imshow(colorIm)

    #plt.subplot(1,2,2)
    #plt.imshow(greyIm, cmap=plt.cm.gray)

    #plt.figure(2)    

    line1, = plt.plot(E, label="Entropy "+str(random[i-1]))

    plt.legend(handler_map={line1: HandlerLine2D(numpoints=4)})



plt.show()



