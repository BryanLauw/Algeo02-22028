import cv2
import numpy as np
import math
import os
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

    cmax, cmin, delta = getCmaxCminDelta(pixel)

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
        

def hsvToVector(blokhsv):
    tinggi, lebar, _ = blokhsv.shape

    array = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    for i in range(tinggi):
        for j in range(lebar):
            h = blokhsv[i][j][0]
            s = blokhsv[i][j][1]
            v = blokhsv[i][j][2] 
            if h >= 316 and h <= 360:
                array[0] += 1
            elif h >= 1 and h <= 25:
                array[1] += 1
            elif h >= 26 and h <= 40:
                array[2] += 1
            elif h >= 41 and h <= 120:
                array[3] += 1
            elif h >= 121 and h <= 190: 
                array[4] += 1
            elif h >= 191 and h <= 270:  
                array[5] += 1
            elif h >= 271 and h <= 295:  
                array[6] += 1
            elif h >= 296 and h <= 315:
                array[7] += 1
            
            if s >= 0 and s < 0.2:
                array[8] += 1
            elif s >= 0.2 and s < 0.7:
                array[9] += 1
            elif s >= 0.7 and s <= 1:
                array[10] += 1

            if v >= 0 and v < 0.2:
                array[11] += 1
            elif v >= 0.2 and v < 0.7:
                array[12] += 1
            elif v >= 0.7 and v <= 1:
                array[13] += 1
        
    return array


def cosineSimilarity(vektor1,vektor2):
    def dot_product(vec1, vec2):
        return sum(x * y for x, y in zip(vec1, vec2))

    def magnitude(vec):
        return math.sqrt(sum(x**2 for x in vec))

    dot_prod = dot_product(vektor1, vektor2)
    mag_vec1 = magnitude(vektor1)
    mag_vec2 = magnitude(vektor2)

    if mag_vec1 == 0 or mag_vec2 == 0:
        return 0  # Avoid division by zero
    
    similarity = dot_prod / (mag_vec1 * mag_vec2)
    return similarity



def normalisasiGambar(arrayRGBGambar1, arrayRGBGambar2):
    arrayRGB1Normal = arrayRGBGambar1 / 255.0
    arrayRGB2Normal = arrayRGBGambar2 / 255.0

    return arrayRGB1Normal, arrayRGB2Normal
    

#ini kalau inputnya langsung rgb gambar
def CosineSimilarityKeseluruhan(rgbgambar1,rgbgambar2):
    normal1, normal2 = normalisasiGambar(rgbgambar1, rgbgambar2)

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


def storeQueryVector(Query):
    arrayQueryBGR = cv2.imread(Query)
    arrayQueryRGB = cv2.cvtColor(np.array(arrayQueryBGR), cv2.COLOR_BGR2RGB)
    arrayQueryNormal = arrayQueryRGB / 255.0
    arrayQueryHSV = convertImagetoHSV(arrayQueryNormal)
    arrayQueryBlock = divide_image_into_blocks(arrayQueryHSV, 4)
    arrayvectorQuery = []
    for i in range(16):
        vectorQueryPerBlock = hsvToVector(arrayQueryBlock[i])
        arrayvectorQuery.append(vectorQueryPerBlock)

    return arrayvectorQuery


def cosineSimilarityForArrayVector(arrayVector1,arrayVector2):
    sum = 0
    for i in range(16):
        sum += cosineSimilarity(arrayVector1[i], arrayVector2[i])

    return sum / 16


def gambar(query, folder):
    vectorQuery = storeQueryVector(query)
    arrayOfArrayVectorDataset = []
    for file in folder:
        file = 'src/static/upload/dir' + file
        vectorForEveryImage = storeQueryVector(file)
        arrayOfArrayVectorDataset.append(vectorForEveryImage)


    arrayCosineSimilarity = []
    for i in arrayOfArrayVectorDataset:
        x = cosineSimilarityForArrayVector(vectorQuery, i)
        arrayCosineSimilarity.append(x)

    return arrayOfArrayVectorDataset

        

# Fungsi Utama
#gambar1 = storeQueryVector("blue.jpg")
#gambar2 = storeQueryVector("yellow.jpg")

#print(cosineSimilarityForArrayVector(gambar1, gambar2))

#gambar1 = cv2.imread("blue.jpg")
#gambar2 = cv2.imread("yellow.jpg")

#arrayRGBGambar1 = cv2.cvtColor(np.array(gambar1), cv2.COLOR_BGR2RGB)


#arrayRGBGambar2 = cv2.cvtColor(np.array(gambar2), cv2.COLOR_BGR2RGB)
#array_rgb_float = array_rgb.astype(np.float32)

#arrayRGB1Normal = arrayRGBGambar1 / 255.0
#arrayRGB2Normal = arrayRGBGambar2 / 255.0

#hasil = CosineSimilarityKeseluruhan(arrayRGBGambar1, arrayRGBGambar2)


#print(hasil)

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


