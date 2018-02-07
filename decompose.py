import assign, settings, os

#define decompose function
def decomp(inXd, inYd, inTd, xmind, xmaxd, ymind, ymaxd, tmind, tmaxd, leveld):
    # inXd: list of x-coordinates \ inYd: list of y-coordinates \ inTd: list of t-coordinates
    # xmind: subdomain lower x boundary \ xmaxd: subdomain upper x boundary \ ymind: subdomain lower x boundary
    # ymaxd: subdomain upper y boundary \ tmind: subdomain lower t boundary \ tmaxd: subdomain upper t boundary
    # leveld: level of recursion

    #subdomain number (identifier)
    settings.sdNum += 1
    # print(settings.sdNum)
    #enforce regular grid
    xminDiff = xmind % settings.p3
    xmaxDiff = xmaxd % settings.p3
    yminDiff = ymind % settings.p3
    ymaxDiff = ymaxd % settings.p3
    tminDiff = tmind % settings.p4
    tmaxDiff = tmaxd % settings.p4

    xminP = xmind - xminDiff + settings.p3
    xmaxP = xmaxd - xmaxDiff + settings.p3
    yminP = ymind - yminDiff + settings.p3
    ymaxP = ymaxd - ymaxDiff + settings.p3
    tminP = tmind - tminDiff + settings.p4
    tmaxP = tmaxd - tmaxDiff + settings.p4

    xC, yC, tC = 0, 0, 0

    xIter = xminP
    while xIter < xmaxP:
        xC += 1
        xIter += settings.p3

    yIter = yminP
    while yIter < ymaxP:
        yC += 1
        yIter += settings.p3

    tIter = tminP
    while tIter < tmaxP:
        tC += 1
        tIter += settings.p4

    xDim = xmaxd - xmind
    yDim = ymaxd - ymind
    tDim = tmaxd - tmind

    sdVolume = xDim * yDim * tDim
    bufVolume = (xDim + 2 * settings.p1) * (yDim + 2 * settings.p1) * (tDim + 2 * settings.p2)
    bufRatio = sdVolume / bufVolume

    if len(inXd) is 0:  # if there are no data points or no regular grid points within subdomain, pass
        pass
    elif xC is 0:
        pass
    elif yC is 0:
        pass
    elif tC is 0:
        pass
    elif len(inXd) <= settings.p5 or bufRatio <= settings.p6:

        fn1 = open(settings.dir1 + os.sep + "pts_" + str(settings.sdNum) + ".txt", "w")
        fn1.write(str(xmind) + ", " + str(xmaxd) + ", " + str(ymind) + ", " + str(ymaxd) + ", " + str(tmind) + ", " + str(tmaxd) + "\n")
        for x, y, t in list(zip(inXd, inYd, inTd)):
            fn1.write(str(x) + ", " + str(y) + ", " + str(t) + "\n")
        fn1.close()

    else:  # if number of points in subdomain is higher than threshold, keep decomposing.
        sdXYZ = assign.ass(inXd, inYd, inTd, xmaxd, xmind, ymaxd, ymind, tmaxd, tmind, leveld)
        decomp(sdXYZ[0], sdXYZ[1], sdXYZ[2], xmind, sdXYZ[-3], ymind, sdXYZ[-2], tmind, sdXYZ[-1], leveld+1)  # recursive function call 1
        decomp(sdXYZ[3], sdXYZ[4], sdXYZ[5], sdXYZ[-3], xmaxd, ymind, sdXYZ[-2], tmind, sdXYZ[-1], leveld+1)  # recursive function call 2
        decomp(sdXYZ[6], sdXYZ[7], sdXYZ[8], xmind, sdXYZ[-3], sdXYZ[-2], ymaxd, tmind, sdXYZ[-1], leveld+1)  # recursive function call 3
        decomp(sdXYZ[9], sdXYZ[10], sdXYZ[11], sdXYZ[-3], xmaxd, sdXYZ[-2], ymaxd, tmind, sdXYZ[-1], leveld+1)  # recursive function call 4
        decomp(sdXYZ[12], sdXYZ[13], sdXYZ[14], xmind, sdXYZ[-3], ymind, sdXYZ[-2], sdXYZ[-1], tmaxd, leveld+1)  # recursive function call 5
        decomp(sdXYZ[15], sdXYZ[16], sdXYZ[17], sdXYZ[-3], xmaxd, ymind, sdXYZ[-2], sdXYZ[-1], tmaxd, leveld+1)  # recursive function call 6
        decomp(sdXYZ[18], sdXYZ[19], sdXYZ[20], xmind, sdXYZ[-3], sdXYZ[-2], ymaxd, sdXYZ[-1], tmaxd, leveld+1)  # recursive function call 7
        decomp(sdXYZ[21], sdXYZ[22], sdXYZ[23], sdXYZ[-3], xmaxd, sdXYZ[-2], ymaxd, sdXYZ[-1], tmaxd, leveld+1)  # recursive function call 8

"""
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
"""