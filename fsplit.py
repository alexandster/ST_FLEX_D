import settings

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
                settings.cList[j] += 1
            elif c1diff < buf and c > i:   #circle cut on right
                pMap[1][j] += 1             #increase number of cut circles
                pMap[2][j] -= 1             #decrease number of data points off-balance
                settings.cList[j] += 1
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

    settings.pList[idx] += 1

    return pMap[0][idx]