#import modules
from datetime import datetime
import sys, os, random

#set recursion limit
sys.setrecursionlimit(4000)

#initialize global variables
#sett.init()

p1, p2, p3 = 25.00,	1.00, 100.000000
# p1 = spatial bandwidth
# p2 = spatial resolution
# p3 = number of points threshold (T1)

#keeps track of the number of cut circles for each candidate split
cList = [0,0,0,0,0]
#stores the number of times each candidate split was chosen
pList = [0,0,0,0,0]


#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#define flex function: finds split that cuts the minimum number of circles among  5 candidate splits
#Parameter 1: input coordinates (1D), Parameter 2: maximum of coordinate range, Parameter 3: minimum of coordinate range, Parameter 4: buffer distance
def flex(inListf, maxf, minf, buf, levelf):

    #increment: divide range of coordinate values by the desired number of candidate splits + 1
    cRange = maxf - minf

    #number of candidate splits
    numCSplits = 5
    numCSplits1 = numCSplits +1
    #data structure to keep track of how many circles cut for each candidate split: [[split coordinates],[number of cut circles],[number of data points off balance],[centrality measure]]
    pMap = [[0]*numCSplits, [0]*numCSplits, [0]*numCSplits, [0]*numCSplits]

    #compute centrality measure
    i = 0
    j = numCSplits - 1
    while i < numCSplits:
        k = range(0, numCSplits)
        pMap[3][i] = k[i] * k[j]
        i += 1
        j -= 1

    #populate first element of pMap with split coordinates
    i = 0
    while i < numCSplits:
        pMap[0][i] = minf + cRange * ((i+1)/numCSplits1)     #split coordinate
        i += 1

    #for each point, for each candidate split, check whether circle is cut. If yes, keep track of count using pMap
    for i in inListf:
        j = 0
        while j < numCSplits:
            c = pMap[0][j]      #candidate partition coordinate
            c1diff = abs(c-i)   #absolute difference data point - candidate partition
            if c1diff < buf and c < i:     #circle cut on left
                pMap[1][j] += 1             #increase number of cut circles
                pMap[2][j] += 1             #increase number of data points off-balance
                cList[j] += 1
            elif c1diff < buf and c > i:   #circle cut on right
                pMap[1][j] += 1             #increase number of cut circles
                pMap[2][j] -= 1             #decrease number of data points off-balance
                cList[j] += 1
            elif c1diff > buf and c < i:   #circle not cut
                pMap[2][j] += 1             #increase number of data points off-balance
            else:
                pMap[2][j] -= 1             #decrease number of data points off-balance
            j += 1

    print(pMap)

    #minimum value of cut circles
    min_value = min(pMap[1])

    #list of indices that point to lowest values in pMap[1]
    x1 = [i for i, x in enumerate(pMap[1]) if x == min_value]

    #if minimum number of cut circles is tied between one or more candidate splits, pick split that partitions points more evenly
    if len(x1) == 1:
        idx = x1[0]
    else:
        #off-balance numbers of candidate splits: index list of off balance numbers with minimum number of cut circles indices
        obnList = [pMap[2][i] for i in x1]
        # minimum value of off-balance number
        min_value = min(obnList, key=abs)
        # list of indices that point to lowest values in pMap[2]
        x2 = [i for i, x in enumerate(pMap[2]) if x == min_value]

        if len(x2) == 1:
            idx = x2[0]
        else:
            #centrality numbers of candidate splits: index list of centrality numbers with minimum off balance numbers
            centList = [pMap[3][i] for i in x2]
            #minimum value of centrality number
            max_value = max(centList, key=abs)
            #list of indices that point to lowest values in pMap[2]
            x3 = [i for i, x in enumerate(pMap[3]) if x == max_value]
            idx = x3[0]

    pList[idx] += 1

    return pMap[0][idx]
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#define assign function
def assign(inXf, xmaxf, xminf, levelf):

    xr2 = flex(inXf, xmaxf, xminf, p1, levelf)     # Subdomain division x coordinates

    sdX1, sdX2 = [],[]    #list of data points for each subdomain (X-coordiantes)

    for x in inXf:       # assign each data point to subdomain
        if x < xr2 - p1:
            sdX1.append(x)

        elif x < xr2 + p1:
            sdX1.append(x)
            sdX2.append(x)

        else:
            sdX2.append(x)


    sdXYZd = [sdX1, sdX2, xr2]

    return sdXYZd

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#define decompose function
def decompose(inXd, xmind, xmaxd, leveld):  # inXd: list of x-coordinates \ inYd: list of y-coordinates \ inZd: list of z-coordinates
# xmind: subdomain lower x boundary \ xmaxd: subdomain upper x boundary \ ymind: subdomain lower x boundary
# ymaxd: subdomain upper y boundary \ zmind: subdomain lower x boundary \ zmaxd: subdomain upper z boundary
# xybufd: spatial buffer \ zbufd: temporal buffer

    xminDiff = xmind % p2
    xmaxDiff = xmaxd % p2
    xminP = xmind - xminDiff + p2
    xmaxP = xmaxd - xmaxDiff + p2

    xC = 0

    xIter = xminP
    while xIter < xmaxP:
        xC += 1
        xIter += p2

    if len(inXd) is 0:  # if there are no data points within subdomain, pass
        pass
    elif xC is 0:       # if there are no grid points within subdomain, pass
        pass
    elif len(inXd) <= p3:

        pass

    else:  # if number of points in subdomain is higher than threshold, keep decomposing.
        sdXYZ = assign(inXd, xmaxd, xmind, leveld)
        decompose(sdXYZ[0], xmind, sdXYZ[-1], leveld+1)  # recursive function call 1
        decompose(sdXYZ[1], sdXYZ[-1], xmaxd, leveld+1)  # recursive function call 2

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#main: start decomposition
out1, out2, out3, out4, out5 = [],[],[],[],[]

numIt = 2       #number of iterations (randomness)
numPts = 1000      #number of data points
minX = 0            #min of range
maxX = 1000         #max of range

i = 0
while i < numIt:

    #keeps track how many circles were cut for each candidate split
    cList = [0,0,0,0,0]

    #create random numbers
    inX  = []
    count = 0
    while count < numPts:
        inX.append(random.uniform(minX,maxX))
        count += 1

    xmin, xmax = 0, 1000
    decompose(inX, xmin, xmax, 0)

    out1.append(cList[0] / numIt)
    out2.append(cList[1] / numIt)
    out3.append(cList[2] / numIt)
    out4.append(cList[3] / numIt)
    out5.append(cList[4] / numIt)

    i += 1

print(sum(out1),sum(out2),sum(out3),sum(out4),sum(out5))
print(pList)
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------











