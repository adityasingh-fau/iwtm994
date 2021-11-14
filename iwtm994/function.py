import numpy as np
import cv2
from ipywidgets import interact, fixed
from PIL import Image
def imshow(X, resize=None):
  
  image = cv2.imread(X)
  if resize != "None" :
    image = np.resize(image,resize)
    cv2_imshow(image) 
    
pass
