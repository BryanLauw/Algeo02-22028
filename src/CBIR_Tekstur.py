import numpy as np
import math as m
import cv2
import os
import time
from zipfile import ZipFile

def nContrast(mCO) :
    contrast = 0
    for i in range(0,256):
        for j in range(0,256):
            contrast = contrast + mCO[i][j]*(m.pow((i-j),2))
    print(contrast)
    return contrast

def nHomogeneity(mCo) :
    homogeneity = 0
    for i in range(0,256):
        for j in range(0,256):
            homogeneity = homogeneity + mCo[i][j]/(1 + (m.pow((i-j),2)))
    print(homogeneity)
    return homogeneity

def nEntropy(mCo) :
    entropy = 0
    for i in range(0,256):
        for j in range(0,256):
            if mCo[i][j] != 0 :
                entropy = entropy - mCo[i][j]*(m.log10(mCo[i][j]))
    print(entropy)
    return entropy

def matriksCoOccurance(mGrayImage) :    
    mCo = np.array([[0.0 for j in range(256)] for i in range(256)])
    for i in range(len(mGrayImage)):
        for j in range(len(mGrayImage[0])-1):
            p = mGrayImage[i][j]
            q = mGrayImage[i][j+1]
            mCo[p][q] = mCo[p][q] + 1
    mCoT = mCo.transpose()
    matriksCO = mCo + mCoT
    sigma = 2*len(mGrayImage)*(len(mGrayImage[0])-1)
    matriksCO = matriksCO/sigma
    return matriksCO

def nDissimilarity(mCo) :
    dissimilarity = 0 
    for i in range(0,256) :
        for j in range(0,256) :
            if i >= j :
                dissimilarity = dissimilarity + mCo[i][j]*(i-j) 
            else :
                dissimilarity = dissimilarity + mCo[i][j]*(j-i)
    #print(dissimilarity)
    return dissimilarity

def nASM(mCo) :
    ASM = 0 
    for i in range(0,256) :
        for j in range(0,256) :
            ASM = ASM + m.pow(mCo[i][j],2)
    #print(ASM)
    return ASM

def nEnergy(mCo) :
    energy = m.sqrt(nASM(mCo))
    #print(energy)
    return energy

def RGBtoGrayscale(gambar) :
    mGray = np.array([[0 for j in range(len(gambar[0]))] for i in range(len(gambar))])
    for i in range(len(gambar)) :
        for j in range(len(gambar[0])) :
            mGray[i][j] = 0.299*gambar[i][j][2] + 0.587*gambar[i][j][1] + 0.114*gambar[i][j][0]
    return mGray

def cosSimilarity(vektorA, vektorB) :
    dotProduct = 0
    for i in range(3) :
        dotProduct = dotProduct + vektorA[i]*vektorB[i] 
    jarakA = 0
    jarakB = 0
    for i in range(3) :
        jarakA = jarakA + m.pow(vektorA[i],2)
        jarakB = jarakB + m.pow(vektorB[i],2)
    jarakA = jarakA*jarakB  
    jarakA = dotProduct/m.sqrt(jarakA)
    return jarakA

def texture(queryImg, zipFolder):
    with ZipFile(zipFolder, 'r') as f :
        f.extractall('dataset')

    folder = os.listdir('dataset')
    array_vektor = []
    for file in folder :
        #start = time.time()
        image = cv2.imread(file)
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
    vektorA = [nContrast(mCO1), nHomogeneity(mCO1), nEntropy(mCO1)]
    vektorB = [nContrast(mCO2), nHomogeneity(mCO2), nEntropy(mCO2)]
    nCossine = cosSimilarity(vektorA,vektorB)
    return nCossine

# image1 = cv2.imread("src/kucing2.jpg")
# image2 = cv2.imread("src/siklus.jpg")
# #image1 = RGBtoGrayscale(image1) 601,2/907,8*401 18178,7
# #image2 = RGBtoGrayscale(image2)
# print(image1)
# print(image2)
# image1 = cv2.cvtColor(np.array(image1), cv2.COLOR_BGR2GRAY)
# image2 = cv2.cvtColor(np.array(image2), cv2.COLOR_BGR2GRAY)
# mCO1 = matriksCoOccurance(image1)
# print(mCO1)
# mCO2 = matriksCoOccurance(image2)
# print(mCO2)
# print(image1)
# print(image2)
# hasil = bandingTekstur(mCO1,mCO2)
# print(hasil)


