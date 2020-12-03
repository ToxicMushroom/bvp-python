import math


def binary_search(sortedlist, needle):
    indexmin = 0
    indexmax = len(sortedlist) - 1
    while indexmin < indexmax:
        indexmid = int(math.floor((indexmax + indexmin) / 2.0))
        if needle <= sortedlist[indexmid]:
            indexmax = indexmid
        else:
            indexmin = indexmid + 1
    if needle == sortedlist[indexmax]:
        return indexmax
    else:
        return None

    #  3(n-1) + 1
    #  O(n)
