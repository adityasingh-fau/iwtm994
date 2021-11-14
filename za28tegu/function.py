import numpy as np
import matplotlib.pyplot as PLT

def imshow(X, resize=None): 
  
  if resize != None :
    X = np.resize(X,resize)
  PLT.imshow(X)    
pass
