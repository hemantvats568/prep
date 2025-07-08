'''
Reverse an array:
def reversearray(l):
    fi=0
    li=len(l)-1
    while fi<=li:
        l[fi],l[li]=l[li],l[fi]
        fi+=1
        li-=1
    return l

print(reversearray(list(map(int,(input("enter array elements: ").split(" "))))))
'''
'''
Left rotate array by d elements. Given an array and we have to left rotate it by d elements.
l = [2,6,8,1,4,9,3]
This approach required O(n) time and O(d) auxiliary space and hence is not the best approach
def rotatearry(l,d):
    temp = l[0:d]
    for i in list(range(len(l)))[d:]:
        l[i-d]=l[i]
    l[len(l)-d:] = temp
    return l
print(rotatearry(l,1))

The following approach requires O(n) time complexity and O(1) auxiliary space. The approach is that we first reverse the first d elements. Then we
reverse the elements from index d to last element. Then we reverse all the elements. The resulting array will be a left rotated array.

import math
l = [2,6,8,1,4,9,3]
# x represents the number of elements in the array to be reversed
def reversearray(l,fi,li):
    while fi<=li:
        l[fi],l[li] = l[li],l[fi]
        fi+=1
        li-=1
    return l

def bestrotatearray(l,d):
    reversearray(l,0,d-1)
    reversearray(l,d,len(l)-1)
    reversearray(l,0,len(l)-1)
    return l

print(bestrotatearray(l,2))
'''

'''
Print all leaders in an array. A leader element is defined as an element for which all elements on it's right are smaller than it.
def printleaders(l):
    i=len(l)-1
    cl = l[i]
    print(l[i])
    l-=1
    while i>=0:
        if l[i]>cl:
            print(l[i])
            cl=l[i]
        i-=1
'''
