import cv2
import numpy as np
import math

def getCmaxCminDelta(pixel):
    cmax = np.max(pixel)
    cmin = np.min(pixel)
    delta = cmax - cmin
    return  cmax, cmin, delta

def convertImagetoHSV(arrayNormal):

    array_hsv = np.zeros_like(arrayNormal)

    for i in range(arrayNormal.shape[0]):
        for j in range(arrayNormal.shape[1]):
            array_hsv[i, j, :] = rgb_to_hsv(arrayNormal[i, j, :])

    
    return array_hsv

def divide_image_into_blocks(image, block_size):
    height, width, _ = image.shape
    blocks = []

    deltaHeight = height // 4
    deltaWidth = width // 4

    for y in range(0, height, deltaHeight):
        for x in range(0, width, deltaWidth):
            block = image[y:y+deltaHeight, x:x+deltaWidth]
            blocks.append(block)

    return blocks

    
def rgb_to_hsv(pixel):
    r = pixel[0]
    g = pixel[1]
    b = pixel[2]

    #print("ini r", pixel[0])
    #print("ini g", pixel[1])
    #print("ini b", pixel[2])

    

    cmax, cmin, delta = getCmaxCminDelta(pixel)


    #print(cmax, cmin, delta)

    if delta == 0:
        h = 0
    else:
        if cmax == r:
            h = 60 * (((g-b)/delta)%6)
        elif cmax == g:
            h = 60 * (((b-r)/delta)+2)
        elif cmax == b:
            h = 60 * (((r-g)/delta) +4)
    if cmax == 0:
        s = 0
    else:
        s = delta/cmax
    
    v = cmax

    return [h, s, v]
        


    #print(h, s, v)

def hsvToVector(blokhsv):
    tinggi, lebar, _ = blokhsv.shape
    sumH = 0
    sumS = 0
    sumV = 0
    for i in range(tinggi):
        for j in range(lebar):
            h = blokhsv[i][j][0]
            s = blokhsv[i][j][1]
            v = blokhsv[i][j][2] 
            if h >= 316 and h <= 360:
                H = 0
                sumH += H
            elif h >= 1 and h <= 25:
                H = 1
                sumH += H
            elif h >= 26 and h <= 40:
                H = 2
                sumH += H
            elif h >= 41 and h <= 120:
                H = 3
                sumH += H
            elif h >= 121 and h <= 190:  
                H = 4  
                sumH += H
            elif h >= 191 and h <= 270:  
                H = 5
                sumH += H
            elif h >= 271 and h <= 295:  
                H = 6 
                sumH += H
            elif h >= 295 and h <= 315:
                H = 7
                sumH += H

            
 

            if s >= 0 and s < 0.2:
                S = 0
                sumS += S
            elif s >= 0.2 and s < 0.7:
                S = 1
                sumS += S
            elif s >= 0.7 and s <= 1:
                S = 2
                sumS += S

            if v >= 0 and v < 0.2:
                V = 0
                sumV += V
            elif v >= 0.2 and v < 0.7:
                V = 1
                sumV += V
            elif v >= 0.7 and v <= 1:
                V = 2
                sumV += V
            

    arr = [sumH/(tinggi*lebar),sumS/(tinggi*lebar), sumV/(tinggi*lebar)] 
    return arr
 
def cosineSimilarity(vektor1,vektor2):
    dot_product = vektor1[0]*vektor2[0] + vektor1[1]*vektor2[1] + vektor1[2] * vektor2[2]
    perkalian_panjang = math.sqrt(math.pow(vektor1[0],2) + math.pow(vektor1[1],2)+math.pow(vektor1[2],2)) * math.sqrt(math.pow(vektor2[0],2)+math.pow(vektor2[1],2) + math.pow(vektor2[2],2))
    return dot_product/perkalian_panjang



def CosineSimilarityKeseluruhan(normal1,normal2):
    array_hsv_gam1 = convertImagetoHSV(normal1)
    array_hsv_gam2 = convertImagetoHSV(normal2)

    blok_gam1 = divide_image_into_blocks(array_hsv_gam1, 4)
    blok_gam2 = divide_image_into_blocks(array_hsv_gam2, 4)

    sum = 0
    len = 0

    for i in range(16):
        vektor1 = hsvToVector(blok_gam1[i])
        vektor2 = hsvToVector(blok_gam2[i])
        #print("ini vektor1",vektor1)
        #print("ini vektor2",vektor2)
        #print("ini vektor1", vektor1)
        #print("ini vektor2", vektor2)
        cosinePerBlok = cosineSimilarity(vektor1, vektor2)
        sum += cosinePerBlok
        len += 1
        #print(cosinePerBlok)
        #print("ini cosine similarity nya", cosinePerBlok)

    return sum/len



    

    


# Fungsi Utama


gambar1 = cv2.imread("yellow.jpg")
gambar2 = cv2.imread("blue.jpg")

arrayRGBGambar1 = cv2.cvtColor(np.array(gambar1), cv2.COLOR_BGR2RGB)


arrayRGBGambar2 = cv2.cvtColor(np.array(gambar2), cv2.COLOR_BGR2RGB)
#array_rgb_float = array_rgb.astype(np.float32)

arrayRGB1Normal = arrayRGBGambar1 / 255.0
arrayRGB2Normal = arrayRGBGambar2 / 255.0

hasil = CosineSimilarityKeseluruhan(arrayRGB1Normal, arrayRGB2Normal)

print(hasil)
#print(arrayRGB1Normal)
#print("ini yang kedua --------------")
#print(arrayRGB2Normal)

#print(cosineSimilarity([1,0,0],[0,0,1]))

#hasil = getAllCmaxCminDelta(array_rgb_normalized)

#arr = arr.astype(np.float64)
#blocks = divide_image_into_blocks(array_rgb_normalized, 4)

#cek = convertImagetoHSV(array_rgb_normalized)

#print(cek[0][0])

#blok = divide_image_into_blocks(cek, 4)

#asil = hsvToVector(blok[0])

#print(cosineSimilarity([1,2,3],[1,2,3]))


#print(blocks[15])

#print(array_rgb[511][511])

#print(array_rgb_normalized[0][0])


#print(hasil[511][511])

#print(array_rgb_normalized[0][1])

#print(blocks[0][0][1])

#print(blocks[0][0][0])

#hasil = convertImagetoHSV(array_rgb_normalized)

#rgb_to_hsv(array_rgb_normalized[0][0])



"""
arr = [22,47,28]
arr = np.array(arr)

arrNorm = arr/ 255.0
cmax, cmin, delta = getCmaxCminDelta(arrNorm)

print(cmax, cmin, delta)

print(arrNorm)
rgb_to_hsv(arrNorm)
"""




#print(hasil)
#print(array_rgb_normalized[0])
#print(hasil[0])
#print(hasil)





"""
print(array_rgb_normalized[0][0])
cmax, cmin, delta = getCmaxCminDelta(array_rgb_normalized)
print(cmax, cmin, delta)
"""

#print(array_rgb_normalized)

#tinggi, lebar, _ = array_rgb.shape

"""
for y in range(10):
    for x in range(10):
        pixel_rgb = array_rgb_normalized[y, x]
        print(f'Pixel di posisi ({x}, {y}): {pixel_rgb}')
"""


#print(getCmaxCminDelta(array_rgb_normalized[0][0][0])+1)


"""
print(array_rgb_normalized[0][0])
print(np.max(array_rgb_normalized[0][0]))
print(getCmaxCminDelta(array_rgb_normalized[0][0]))
cmax , cmin, delta = getCmaxCminDelta(array_rgb_normalized[0][0])
print(cmax)
"""


