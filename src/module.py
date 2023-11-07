import numpy as np
import cv2

def extractRGBMat(x):
    # Menghasilkan matriks RGB gambar untuk setiap pikselnya
    img = cv2.imread(x,1)
    red = img[:,:,2]
    green = img[:,:,1]
    blue = img[:,:,0]
    mat = np.dstack([red,green,blue])
    return mat