import cv2
import numpy as np
import math

def getCmaxCminDelta(pixel):
    cmax = np.max(pixel)
    cmin = np.min(pixel)
    delta = cmax - cmin
    return  cmax, cmin, delta

def divide_image_into_blocks(image, block_size):
    height, width, _ = image.shape

    delta_height = height // 4
    delta_width = width // 4

    blocks = [image[y:y+delta_height, x:x+delta_width] for y in range(0, height, delta_height) for x in range(0, width, delta_width)]

    return blocks

def imageToVector(arrayNormal):
    array = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    for i in range(arrayNormal.shape[0]):
        for j in range(arrayNormal.shape[1]):
            h, s, v = rgb_to_hsv(arrayNormal[i, j, :])
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

    return h, s, v


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

def storeQueryVector(Query):
    arrayQueryBGR = cv2.imread(Query)
    arrayQueryRGB = cv2.cvtColor(np.array(arrayQueryBGR), cv2.COLOR_BGR2RGB)
    arrayQueryNormal = arrayQueryRGB / 255.0
    arrayQueryBlock = divide_image_into_blocks(arrayQueryNormal, 4)
    arrayvectorQuery = []
    for i in range(16):
        vectorQueryPerBlock = imageToVector(arrayQueryBlock[i])
        arrayvectorQuery.append(vectorQueryPerBlock)

    return arrayvectorQuery

def cosineSimilarityForArrayVector(arrayVector1,arrayVector2):
    sum = 0
    for i in range(16):
        sum += cosineSimilarity(arrayVector1[i], arrayVector2[i])

    return sum / 16


# start = time.time()  

# vektor1 = storeQueryVector("src/anna-bisso.jpg")
# vektor2 = storeQueryVector("src/yellow.jpg")

# print(cosineSimilarityForArrayVector(vektor1, vektor2))

# end = time.time()
# print(f"Time taken: {(end-start)*10**3:.03f}ms")


def color(query, folder):
    vectorQuery = storeQueryVector(query)
    arrayOfArrayVectorDataset = []
    for file in folder:
        file = 'src/static/upload/dir/' + file
        vectorForEveryImage = storeQueryVector(file)
        arrayOfArrayVectorDataset.append(vectorForEveryImage)


    arrayCosineSimilarity = []
    for i in arrayOfArrayVectorDataset:
        x = round(cosineSimilarityForArrayVector(vectorQuery, i)*100,2)
        arrayCosineSimilarity.append(x)

    return arrayCosineSimilarity

def urutGambarWarna(ar_cos,ar_file) :
    a = [(ar_cos[i],ar_file[i]) for i in range(len(ar_cos))]
    gambarUrut = list(filter(lambda x: x[0] >= 60, a))
    gambarUrut.sort(reverse=True)
    return gambarUrut


