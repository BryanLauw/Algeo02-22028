import numpy as np
import math as m
import cv2
import os
import time
from zipfile import ZipFile

def nContrast(mCo):
    i, j = np.indices(mCo.shape)
    contrast = np.sum(mCo * (i - j)**2)
    return contrast

def nHomogeneity(mCo):
    i, j = np.indices(mCo.shape)
    homogeneity = np.sum(mCo / (1 + (i - j)**2))
    return homogeneity

def nEntropy(mCo):
    non_zero_elements = mCo[mCo != 0]
    entropy = -np.sum(non_zero_elements * np.log10(non_zero_elements))
    return entropy

def nDissimilarity(mCo):
    i, j = np.indices(mCo.shape)
    dissimilarity = np.sum(mCo * np.abs(i - j))
    return dissimilarity

def nASM(mCo):
    asm = np.sum(mCo**2)
    return asm

def nEnergy(mCo):
    energy = m.sqrt(nASM(mCo))
    return energy


# def nContrast(mCO) :
#     contrast = 0
#     for i in range(0,256):
#         for j in range(0,256):
#             contrast = contrast + mCO[i][j]*(m.pow((i-j),2))
#     # print(contrast)
#     return contrast

# def nHomogeneity(mCo) :
#     homogeneity = 0
#     for i in range(0,256):
#         for j in range(0,256):
#             homogeneity = homogeneity + mCo[i][j]/(1 + (m.pow((i-j),2)))
#     # print(homogeneity)
#     return homogeneity

# def nEntropy(mCo) :
#     entropy = 0
#     for i in range(0,256):
#         for j in range(0,256):
#             if mCo[i][j] != 0 :
#                 entropy = entropy - mCo[i][j]*(m.log10(mCo[i][j]))
#     # print(entropy)
#     return entropy

# def nDissimilarity(mCo) :
#     dissimilarity = 0 
#     for i in range(0,256) :
#         for j in range(0,256) :
#             if i >= j :
#                 dissimilarity = dissimilarity + mCo[i][j]*(i-j) 
#             else :
#                 dissimilarity = dissimilarity + mCo[i][j]*(j-i)
#     #print(dissimilarity)
#     return dissimilarity

# def nASM(mCo) :
#     ASM = 0 
#     for i in range(0,256) :
#         for j in range(0,256) :
#             ASM = ASM + m.pow(mCo[i][j],2)
#     #print(ASM)
#     return ASM

# def nEnergy(mCo) :
#     energy = m.sqrt(nASM(mCo))
#     #print(energy)
#     return energy

import numpy as np

def matriksCoOccurance(mGrayImage):
    mCo = np.zeros((256, 256), dtype=float)

    for i in range(len(mGrayImage)):
        p = mGrayImage[i, :-1]
        q = mGrayImage[i, 1:]
        np.add.at(mCo, (p, q), 1)

    matriksCO = mCo + mCo.transpose()
    sigma = 2 * len(mGrayImage) * (len(mGrayImage[0]) - 1)
    matriksCO /= sigma

    return matriksCO

# def matriksCoOccurance(mGrayImage) :    
#     mCo = np.array([[0.0 for j in range(256)] for i in range(256)])
#     for i in range(len(mGrayImage)):
#         for j in range(len(mGrayImage[0])-1):
#             p = mGrayImage[i][j]
#             q = mGrayImage[i][j+1]
#             mCo[p][q] = mCo[p][q] + 1
#     mCoT = mCo.transpose()
#     matriksCO = mCo + mCoT
#     sigma = 2*len(mGrayImage)*(len(mGrayImage[0])-1)
#     matriksCO = matriksCO/sigma
#     return matriksCO

# def RGBtoGrayscale(gambar) :
#     start = time.time()
#     mGray = np.array([[0 for j in range(len(gambar[0]))] for i in range(len(gambar))])
#     for i in range(len(gambar)) :
#         for j in range(len(gambar[0])) :
#             mGray[i][j] = 0.299*gambar[i][j][2] + 0.587*gambar[i][j][1] + 0.114*gambar[i][j][0]
#     end = time.time()
#     print(f"Iteration: {1}\tTime taken: {(end-start)*10**3:.03f}ms")
#     return mGray

def RGBtoGrayscale(gambar):
    start = time.time()
    # Extract the RGB channels
    red_channel = gambar[:, :, 2]
    green_channel = gambar[:, :, 1]
    blue_channel = gambar[:, :, 0]
    # Convert RGB to grayscale using the formula: 0.299*R + 0.587*G + 0.114*B
    mGray_float = 0.299 * red_channel + 0.587 * green_channel + 0.114 * blue_channel + 0.5
    mGray = mGray_float.astype(np.uint8)
    end = time.time()
    print(f"Iteration: {1}\tTime taken: {(end-start)*10**3:.03f}ms")
    return mGray


def cosSimilarity(vektorA, vektorB) :
    dotProduct = 0
    for i in range(6) :
        dotProduct = dotProduct + vektorA[i]*vektorB[i] 
    jarakA = 0
    jarakB = 0
    for i in range(6) :
        jarakA = jarakA + m.pow(vektorA[i],2)
        jarakB = jarakB + m.pow(vektorB[i],2)
    jarakA = jarakA*jarakB  
    jarakA = dotProduct/m.sqrt(jarakA)
    return round(jarakA*100,2)

def texture(queryImg, folder):
    array_vektor = []
    for file in folder :
        #start = time.time()
        file = 'src/static/upload/dir/' + file
        image = cv2.imread(file)
        #print(image)
        image = RGBtoGrayscale(image)
        image = matriksCoOccurance(image)
        vektor = [nContrast(image), nHomogeneity(image), nEntropy(image), nDissimilarity(image), nASM(image), nEnergy(image)]
        array_vektor.append(vektor)
        #end = time.time()
        #print(f"Iteration: {file}\tTime taken: {(end-start)*10**3:.03f}ms")
    #print(array_vektor)

    array_cos =[]
    #start = time.time()   
    image = cv2.imread(queryImg)
    image = RGBtoGrayscale(image)
    image = matriksCoOccurance(image)
    vektorq = [nContrast(image), nHomogeneity(image), nEntropy(image), nDissimilarity(image), nASM(image), nEnergy(image)]
    for i in array_vektor :
        x = cosSimilarity(vektorq,i)
        array_cos.append(x)
    #print(array_cos)
    #end = time.time()
    #print(f"Iteration: {file}\tTime taken: {(end-start)*10**3:.03f}ms")
    return array_cos

def bandingTekstur(mCO1, mCO2) :
    vektorA = [nContrast(mCO1), nHomogeneity(mCO1), nEntropy(mCO1),nDissimilarity(mCO1), nASM(mCO1), nEnergy(mCO1)]
    vektorB = [nContrast(mCO2), nHomogeneity(mCO2), nEntropy(mCO2),nDissimilarity(mCO2), nASM(mCO2), nEnergy(mCO2)]
    nCossine = cosSimilarity(vektorA,vektorB)
    return nCossine

start = time.time()
image1 = cv2.imread("src/static/upload/basis.png")
image2 = cv2.imread("src/static/upload/basis.png")
#image1 = RGBtoGrayscale(image1) 601,2/907,8*401 18178,7
image2 = RGBtoGrayscale(image2)
print(image1)
print(image2)
image1 = cv2.cvtColor(np.array(image1), cv2.COLOR_BGR2GRAY)
# image2 = cv2.cvtColor(np.array(image2), cv2.COLOR_BGR2GRAY)
mCO1 = matriksCoOccurance(image1)
print(mCO1)
mCO2 = matriksCoOccurance(image2)
print(mCO2)
print(image1)
print(image2)
hasil = bandingTekstur(mCO1,mCO2)
print(hasil)
end = time.time()
print(f"Iteration: {1}\tTime taken: {(end-start)*10**3:.03f}ms")


#contoh cara pakenya di bawah
def urutGambar(ar_cos, ar_file):
    gambarUrut = [(cos, file) for cos, file in zip(ar_cos, ar_file) if cos >= 60]
    gambarUrut.sort(reverse=True)
    return gambarUrut

def urutGambar(ar_cos,ar_file) :
    a = [(ar_cos[i],ar_file[i]) for i in range(len(ar_cos))]
    # print(a)
    gambarUrut = list(filter(lambda x: x[0] >= 60, a))
    gambarUrut.sort(reverse=True)
    # print(gambarUrut)
    return gambarUrut

# image = cv2.imread('src/static/upload/basis.png')
# image0 = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# image1 = RGBtoGrayscale(image)
# image2 = RGBtoGrayscaleGPT(image)
# print(image0)
# print(image1)
# print(image2)
# folder = os.listdir("src/static/upload/dir")
# ar_file = []
# for file in folder :
#     ar_file.append(file)
# ar_cos = texture("src/static/upload/basis.png",folder)
# ar_gambarUrut = urutGambar(ar_cos,ar_file)
