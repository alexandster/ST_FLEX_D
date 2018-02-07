# settings.py

# sdNum = subdomain number
# p1 = spatial bandwidth
# p2 = temporal bandwidth
# p3 = spatial resolution
# p4 = temporal resolution
# p5 = number of points threshold (T1)
# p6 = buffer ratio threshold (T2)
# dir1 = point files (resulting from decomposition)
# dir2 = time files (resulting from decomposition)
# cList = keeps track of the number of cut circles for each candidate split
# pList = stores the number of times each candidate split was chosen

def init():
    global sdNum, p1, p2, p3, p4, p5, p6, dir1, dir2, pList, cList
    sdNum, p1, p2, p3, p4, p5, p6, dir1, dir2, pList, cList = 0, 0, 0, 0, 0, 0, 0, 0, 0, [0,0,0,0,0], [0,0,0,0,0]


