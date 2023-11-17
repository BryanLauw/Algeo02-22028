import numpy as np
import math as m
import cv2

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


def RGBtoGrayscale(gambar):
    # Extract the RGB channels
    red_channel = gambar[:, :, 2]
    green_channel = gambar[:, :, 1]
    blue_channel = gambar[:, :, 0]
    # Convert RGB to grayscale using the formula: 0.299*R + 0.587*G + 0.114*B
    mGray_float = 0.299 * red_channel + 0.587 * green_channel + 0.114 * blue_channel + 0.5
    mGray = mGray_float.astype(np.uint8)
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
        file = 'src/static/upload/dir/' + file
        image = cv2.imread(file)
        image = RGBtoGrayscale(image)
        image = matriksCoOccurance(image)
        vektor = [nContrast(image), nHomogeneity(image), nEntropy(image), nDissimilarity(image), nASM(image), nEnergy(image)]
        array_vektor.append(vektor)

    array_cos =[]
    image = cv2.imread(queryImg)
    image = RGBtoGrayscale(image)
    image = matriksCoOccurance(image)
    vektorq = [nContrast(image), nHomogeneity(image), nEntropy(image), nDissimilarity(image), nASM(image), nEnergy(image)]
    for i in array_vektor :
        x = cosSimilarity(vektorq,i)
        array_cos.append(x)
    return array_cos

def bandingTekstur(mCO1, mCO2) :
    vektorA = [nContrast(mCO1), nHomogeneity(mCO1), nEntropy(mCO1),nDissimilarity(mCO1), nASM(mCO1), nEnergy(mCO1)]
    vektorB = [nContrast(mCO2), nHomogeneity(mCO2), nEntropy(mCO2),nDissimilarity(mCO2), nASM(mCO2), nEnergy(mCO2)]
    nCossine = cosSimilarity(vektorA,vektorB)
    return nCossine

def urutGambar(ar_cos,ar_file) :
    a = [(ar_cos[i],ar_file[i]) for i in range(len(ar_cos))]
    # print(a)
    gambarUrut = list(filter(lambda x: x[0] >= 60, a))
    gambarUrut.sort(reverse=True)
    # print(gambarUrut)
    return gambarUrut