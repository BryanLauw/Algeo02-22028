from CBIR_Tekstur import *

def bandingTekstur(img1, img2) :
    image1 = cv2.cvtColor(np.array(img1), cv2.COLOR_BGR2GRAY)
    image2 = cv2.cvtColor(np.array(img2), cv2.COLOR_BGR2GRAY)
    mCO1 = matriksCoOccurance(image1)
    mCO2 = matriksCoOccurance(image2)
    vektorA = [nContrast(mCO1), nHomogeneity(mCO1), nEntropy(mCO1)]
    vektorB = [nContrast(mCO2), nHomogeneity(mCO2), nEntropy(mCO2)]
    nCossine = cosSimilarity(vektorA,vektorB)
    return nCossine