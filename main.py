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
# pFile = open('files/parameterFile.txt', "r")
pFile = open('files/parameterFile_data.txt', "r")
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
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#read input point file
# pFile = open('files/AllCases2010_11_clip.txt', "r")
pFile = open('files/data.txt', "r")
inX, inY, inT = [], [], []
r = pFile.readline().split(",")
xmin, xmax, ymin, ymax, tmin, tmax = float(r[0]), float(r[1]), float(r[2]), float(r[3]), float(r[4]), float(r[5].strip())

for record in pFile:
	inX.append(float(record.split(",")[0]))
	inY.append(float(record.split(",")[1]))
	inT.append(float(record.split(",")[2]))
pFile.close()

#keeps track how many circles were cut for each candidate split
settings.cList = [0,0,0,0,0]

decompose.decomp(inX, inY, inT, xmin, xmax, ymin, ymax, tmin, tmax, 0)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#print stuff
#print(sum(out1),sum(out2),sum(out3),sum(out4),sum(out5))
print(settings.pList)
print(settings.sdNum)
print(settings.cList)
