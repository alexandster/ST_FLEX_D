import settings, fsplit

#define assign function
def ass(inXf, inYf, inTf, xmaxf, xminf, ymaxf, yminf, tmaxf, tminf, levelf):
    # inXf: list of x-coordinates \ inYf: list of y-coordinates \ inTf: list of t-coordinates
    # xminf: subdomain lower x boundary \ xmaxf: subdomain upper x boundary \ yminf: subdomain lower y boundary
    # ymaxf: subdomain upper y boundary \ tminf: subdomain lower t boundary \ tmaxf: subdomain upper t boundary
    # levelf: level of recursion

    xr2 = fsplit.flex(inXf, xmaxf, xminf, settings.p1, levelf)     # Subdomain division x coordinates
    yr2 = fsplit.flex(inYf, ymaxf, yminf, settings.p1, levelf)  # Subdomain division x coordinates
    tr2 = fsplit.flex(inTf, tmaxf, tminf, settings.p3, levelf)  # Subdomain division x coordinates

    sdX1, sdX2, sdX3, sdX4, sdX5, sdX6, sdX7, sdX8 = [],[],[],[],[],[],[],[]    #list of data points for each subdomain (X-coordiantes)
    sdY1, sdY2, sdY3, sdY4, sdY5, sdY6, sdY7, sdY8 = [],[],[],[],[],[],[],[]    #list of data points for each subdomain (Y-coordiantes)
    sdT1, sdT2, sdT3, sdT4, sdT5, sdT6, sdT7, sdT8 = [],[],[],[],[],[],[],[]    #list of data points for each subdomain (Z-coordiantes)

    for x, y, t in zip(inXf, inYf, inTf):       # assign each data point to subdomain
        if x < xr2 - settings.p1:
            if y < yr2 - settings.p1:
                if t < tr2 - settings.p3:
                    sdX1.append(x), sdY1.append(y), sdT1.append(t)
                elif t < tr2 + settings.p3:
                    sdX1.append(x), sdY1.append(y), sdT1.append(t)
                    sdX5.append(x), sdY5.append(y), sdT5.append(t)
                else:
                    sdX5.append(x), sdY5.append(y), sdT5.append(t)
            elif y < yr2 + settings.p1:
                if t < tr2 - settings.p3:
                    sdX1.append(x), sdY1.append(y), sdT1.append(t)
                    sdX3.append(x), sdY3.append(y), sdT3.append(t)
                elif t < tr2 + settings.p3:
                    sdX1.append(x), sdY1.append(y), sdT1.append(t)
                    sdX3.append(x), sdY3.append(y), sdT3.append(t)
                    sdX5.append(x), sdY5.append(y), sdT5.append(t)
                    sdX7.append(x), sdY7.append(y), sdT7.append(t)
                else:
                    sdX5.append(x), sdY5.append(y), sdT5.append(t)
                    sdX7.append(x), sdY7.append(y), sdT7.append(t)
            else:
                if t < tr2 - settings.p3:
                    sdX3.append(x), sdY3.append(y), sdT3.append(t)
                elif t < tr2 + settings.p3:
                    sdX3.append(x), sdY3.append(y), sdT3.append(t)
                    sdX7.append(x), sdY7.append(y), sdT7.append(t)
                else:
                    sdX7.append(x), sdY7.append(y), sdT7.append(t)
        elif x < xr2 + settings.p1:
            if y < yr2 - settings.p1:
                if t < tr2 - settings.p3:
                    sdX1.append(x), sdY1.append(y), sdT1.append(t)
                    sdX2.append(x), sdY2.append(y), sdT2.append(t)
                elif t < tr2 + settings.p3:
                    sdX1.append(x), sdY1.append(y), sdT1.append(t)
                    sdX2.append(x), sdY2.append(y), sdT2.append(t)
                    sdX5.append(x), sdY5.append(y), sdT5.append(t)
                    sdX6.append(x), sdY6.append(y), sdT6.append(t)
                else:
                    sdX5.append(x), sdY5.append(y), sdT5.append(t)
                    sdX6.append(x), sdY6.append(y), sdT6.append(t)
            elif y < yr2 + settings.p1:
                if t < tr2 - settings.p3:
                    sdX1.append(x), sdY1.append(y), sdT1.append(t)
                    sdX2.append(x), sdY2.append(y), sdT2.append(t)
                    sdX3.append(x), sdY3.append(y), sdT3.append(t)
                    sdX4.append(x), sdY4.append(y), sdT4.append(t)
                elif t < tr2 + settings.p3:
                    sdX1.append(x), sdY1.append(y), sdT1.append(t)
                    sdX2.append(x), sdY2.append(y), sdT2.append(t)
                    sdX3.append(x), sdY3.append(y), sdT3.append(t)
                    sdX4.append(x), sdY4.append(y), sdT4.append(t)
                    sdX5.append(x), sdY5.append(y), sdT5.append(t)
                    sdX6.append(x), sdY6.append(y), sdT6.append(t)
                    sdX7.append(x), sdY7.append(y), sdT7.append(t)
                    sdX8.append(x), sdY8.append(y), sdT8.append(t)
                else:
                    sdX5.append(x), sdY5.append(y), sdT5.append(t)
                    sdX6.append(x), sdY6.append(y), sdT6.append(t)
                    sdX7.append(x), sdY7.append(y), sdT7.append(t)
                    sdX8.append(x), sdY8.append(y), sdT8.append(t)
            else:
                if t < tr2 - settings.p3:
                    sdX3.append(x), sdY3.append(y), sdT3.append(t)
                    sdX4.append(x), sdY4.append(y), sdT4.append(t)
                elif t < tr2 + settings.p3:
                    sdX3.append(x), sdY3.append(y), sdT3.append(t)
                    sdX4.append(x), sdY4.append(y), sdT4.append(t)
                    sdX7.append(x), sdY7.append(y), sdT7.append(t)
                    sdX8.append(x), sdY8.append(y), sdT8.append(t)
                else:
                    sdX7.append(x), sdY7.append(y), sdT7.append(t)
                    sdX8.append(x), sdY8.append(y), sdT8.append(t)
        else:
            if y < yr2 - settings.p1:
                if t < tr2 - settings.p3:
                    sdX2.append(x), sdY2.append(y), sdT2.append(t)
                elif t < tr2 + settings.p3:
                    sdX2.append(x), sdY2.append(y), sdT2.append(t)
                    sdX6.append(x), sdY6.append(y), sdT6.append(t)
                else:
                    sdX6.append(x), sdY6.append(y), sdT6.append(t)
            elif y < yr2 + settings.p1:
                if t < tr2 - settings.p3:
                    sdX2.append(x), sdY2.append(y), sdT2.append(t)
                    sdX4.append(x), sdY4.append(y), sdT4.append(t)
                elif t < tr2 + settings.p3:
                    sdX2.append(x), sdY2.append(y), sdT2.append(t)
                    sdX4.append(x), sdY4.append(y), sdT4.append(t)
                    sdX6.append(x), sdY6.append(y), sdT6.append(t)
                    sdX8.append(x), sdY8.append(y), sdT8.append(t)
                else:
                    sdX6.append(x), sdY6.append(y), sdT6.append(t)
                    sdX8.append(x), sdY8.append(y), sdT8.append(t)
            else:
                if t < tr2 - settings.p3:
                    sdX4.append(x), sdY4.append(y), sdT4.append(t)
                elif t < tr2 + settings.p3:
                    sdX4.append(x), sdY4.append(y), sdT4.append(t)
                    sdX8.append(x), sdY8.append(y), sdT8.append(t)
                else:
                    sdX8.append(x), sdY8.append(y), sdT8.append(t)

    sdXYZd = [sdX1, sdY1, sdT1, sdX2, sdY2, sdT2, sdX3, sdY3, sdT3, sdX4, sdY4, sdT4, sdX5, sdY5, sdT5, sdX6, sdY6, sdT6, sdX7, sdY7, sdT7, sdX8, sdY8, sdT8, xr2, yr2, tr2]

    return sdXYZd
"""
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
"""