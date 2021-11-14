import numpy as np
import matplotlib.pyplot as PLT
import imageio as io

def imshow(X, resize=None): 
  image = io.imread(X)
  
  if resize != None :
    image = np.resize(image,resize)
    
    PLT.imshow(image)    
pass
