#import modules
from datetime import datetime
import sys, os, random
import decompose, settings

#set recursion limit
sys.setrecursionlimit(4000)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#initialize global variables
settings.init()

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#read parameters
pFile = open('files/parameterFile.txt', "r")
pFile.readline()
pList = pFile.readline().split("\t")

settings.p1 = float(pList[0])	# p1 = spatial bandwidth
settings.p2 = float(pList[1])	# p2 = temporal bandwidth
settings.p3 = float(pList[2])	# p3 = spatial resolution
settings.p4 = float(pList[3])	# p4 = temporal resolution
settings.p5 = float(pList[4])   # p5 = number of points threshold (T1)
settings.p6 = float(pList[5])   # p6 = buffer ratio threshold (T2)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#create output directory
settings.dir1 = 'pointFiles'
if not os.path.exists(settings.dir1):
    os.makedirs(settings.dir1)

settings.dir2 = 'timeFiles'
if not os.path.exists(settings.dir2):
    os.makedirs(settings.dir2)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#keeps track of the number of cut circles for each candidate split
# settings.cList = [0,0,0,0,0]
#stores the number of times each candidate split was chosen
# settings.pList = [0,0,0,0,0]

#for each candidate split, store average number of cut circles for each candidate split
out1, out2, out3, out4, out5 = [],[],[],[],[]

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#more parameters
numIt = 2       #number of iterations (randomness)
numPts = 1000      #number of data points
minXY = 0            #min of spatial range
maxXY = 1000         #max of spatial range
minT = 0            #min of temporal range
maxT = 365         #max of temporal range
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#decompose a number of times (numIt). Because random datasets are created.
i = 0
while i < numIt:

    #keeps track how many circles were cut for each candidate split
    settings.cList = [0,0,0,0,0]

    #create random numbers
    inX  = []
    inY = []
    inT = []

    count = 0
    while count < numPts:
        inX.append(random.uniform(minXY, maxXY))
        inY.append(random.uniform(minXY, maxXY))
        inT.append(random.randint(minT, maxT))
        count += 1

    xmin, xmax = 0, 1000
    decompose.decomp(inX, inY, inT, minXY, maxXY, minXY, maxXY, minT, maxT, 0)

    out1.append(settings.cList[0] / numIt)
    out2.append(settings.cList[1] / numIt)
    out3.append(settings.cList[2] / numIt)
    out4.append(settings.cList[3] / numIt)
    out5.append(settings.cList[4] / numIt)

    i += 1
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

print(sum(out1),sum(out2),sum(out3),sum(out4),sum(out5))
print(settings.pList)
