# coding=UTF-8

list = [-1, 3, 4]

def findMinAndMax(list):
    if(len(list)==0):
        return None,None
    min = list[0]
    max = min
    for x in list:
        if x>=max:
            max = x
        if x<= min:
            min = x
    return (min, max)


print(findMinAndMax(list))