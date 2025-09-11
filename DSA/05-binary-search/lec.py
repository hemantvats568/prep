'''
Binary search iterative
a=[10,20,30,40,50]

def binSearch(n,a):
    i=0
    e=len(a)-1

    while i<=e:
        mid=(i+e)//2
        if a[mid]==n:
            return mid
        elif a[mid]>n:
            e=mid-1
        elif a[mid]<n:
            i=mid+1
        else:
            return None


print(binSearch(35,a))
'''

'''
Recursive binary search

a=[10,20,30,40,50]

def binSearch(n,a,i=0,e=None):
    if e==None:
        e=len(a)-1
    if i>e:
        return None
    mid=(i+e)//2
    if a[mid]==n:
        return mid
    elif a[mid] > n:
        return binSearch(n,a,i,mid-1)
    elif a[mid] < n:
        return binSearch(n,a,mid+1,e)
    else:
        return None
print(binSearch(50,a))
'''

'''
Index of first occurance
a=[1,10,10,10,20,20,40]

def firstOccur(n,a):
    i=0
    e=len(a)-1
    while i<=e:
        mid=(i+e)//2
        if a[mid]==n and a[mid-1]<n:
            return mid
        elif a[mid]==n and mid==0:
            return mid
        elif a[mid]==n and a[mid-1]==n:
            e=mid-1
        elif a[mid] < n:
            i=mid+1
        elif a[mid] > n:
            e=mid-1
    return None

print(firstOccur(1,a))
'''

'''
Index of last occurance of n in a
a=[1,10,10,10,20,20,40]

def lastOccur(n,a):
    i=0
    e=len(a)-1
    while i<=e:
        mid=(i+e)//2
        if a[mid] < n:
            i=mid+1
        elif a[mid] > n:
            e=mid-1
        else:
            if mid==len(a)-1:
                return mid
            elif a[mid+1]==n:
                i=mid+1
            else:
                return mid
    return None

print(lastOccur(1,a))
'''

'''
count occurances in a sorted array
def countOccur(n,a):
    if firstOccur(n,a)!=None:
        return lastOccur(n,a)-firstOccur(n,a) + 1
    return 0

print(countOccur(50,a))
'''

'''
Count 1's in a sorted binary array
a=[0,1]

def oneOccur(a):
    i=0
    e=len(a)-1
    while i<=e:
        mid=(i+e)//2
        if a[mid]==1 and a[mid-1]<1:
            return len(a)-mid
        elif a[mid]==1 and mid==0:
            return len(a)-mid
        elif a[mid]==1 and a[mid-1]==1:
            e=mid-1
        elif a[mid] < 1:
            i=mid+1
        elif a[mid] > 1:
            e=mid-1
    return 0

print(oneOccur(a))
'''

'''
Return floor of square root of a number n
n=22

def floorSquareRoot(n):
    i=1
    e=n
    while i<=e:
        mid=(i+e)//2
        if mid*mid==n:
            return mid
        elif mid*mid > n:
            e=mid-1
        else:
            i=mid+1
            ans=mid
    return ans

print(floorSquareRoot(16))
'''

'''
Search in an infinite sorted array
a=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

def searchInfiniteArr(n,a):
    lastGreatest=1
    if a[0]==n:
        return 0

    while a[lastGreatest]<n:
        lastGreatest=lastGreatest*2

    i=lastGreatest//2+1
    e=lastGreatest

    while i<=e:
        mid=(i+e)//2
        if a[mid]>n:
            e=mid-1
        elif a[mid]<n:
            i=mid+1
        else:
            return mid

    return None

print(searchInfiniteArr(14,a))
'''

'''
Search in sorted rotated array
a=[16,20,7,8,9,10,11,12,13]
def searchRotated(n,a):
    i=0
    e=len(a)-1

    while i<=e:
        mid=(i+e)//2
        if a[mid]==n:
            return mid

        if a[0]<a[mid]: # left side sorted
            if a[mid] > n and a[0]<=n:
                e=mid-1
            else:
                i=mid+1
        else: # Right side sorted
            if a[mid]<n and a[len(a)-1]>=n:
                i=mid+1
            else:
                e=mid-1
    return None

print(searchRotated(6,a))
'''
'''
Finding a peak element in an unsorted array. An element is called a peak element if it is greater than it's neighbours

a=[1,2,0,4]

def findPeak(a):
    i=0
    e=len(a)-1

    if len(a)==1:
        return a[0]
    if len(a)==0:
        return None
    while i<=e:
        mid=(i+e)//2
        if mid==len(a)-1 and a[mid]>a[mid-1]:
            return a[mid]
        elif mid==0 and a[0]>a[1]:
            return a[mid]
        elif a[mid]>a[mid-1] and a[mid]<a[mid+1]:
            i=mid+1
        elif a[mid] < a[mid-1] and a[mid] > a[mid+1]:
            e=mid-1
        else:
            return a[mid]

print(findPeak(a))
'''

'''
2 Pointers approach: Find if there is a pair with sum x in a sorted array
a=[2,5,8,12,30]

def twoPointer(x,a):
    i=0
    e=len(a)-1

    while i<=e:
        if a[i]+a[e]==x:
            return [a[i],a[e]]
        elif a[i]+a[e]>x:
            e-=1
        else:
            i+=1
    return None

print(twoPointer(320,a))
'''

'''
Triplet in a sorted array: in a sorted array find a triplet with given sum x
a=[2,5,8,12,30]

def twoPointer(x,a):
    i=0
    e=len(a)-1

    while i<=e:
        if a[i]+a[e]==x:
            return [a[i],a[e]]
        elif a[i]+a[e]>x:
            e-=1
        else:
            i+=1
    return None

def triplet(x,a):
    i=0

    while i<len(a)-2:
        if twoPointer(x-a[i],a):
            p,q=twoPointer(x-a[i],a)
            return [a[i],p,q]
        else:
            i+=1
    return None

print(triplet(15,a))
'''

'''
Median of two sorted arrays: If both merged middle element or average of middle elements if total elements even
a=[10,20,30,40,50]
b=[5,15,25,35,45]

# [5,10,15,20,25,30,35,45,40,50]
def findMedian(a,b):
    if len(a)>len(b):
        a,b=b,a
    ai=len(a)//2
    bi=(len(a)+len(b)+1)//2 - ai

    if (len(a)+len(b))%2==0:
        is_even=True
    else:
        is_even=False
    while ai < len(a):
        if a[ai] < b[bi-1]:
            ai+=1
            bi-=1
        elif a[ai-1] > b[bi]:
            bi+=1
            ai-=1
        else:
            if is_even:
                return (max(a[ai-1],b[bi-1])+min(a[ai],b[bi]))/2
            else:
                return max(a[ai-1],b[bi-1])


print(findMedian(a,b))
'''

'''
Repeating element:
0<=max_arr<=n-2
Non sorted arrary and only one element repeats
0 to max_arr all elements presents

Linear solution with O(N) auxiliary space

def findRepeating(a):
    bool_arr=[False]*len(a)
    i=0
    while i<len(a):
        if bool_arr[a[i]]:
            return a[i]
        else:
            bool_arr[a[i]]=True

        i+=1

solution in O(n) time and O(1) space complexity

a=[0,2,1,3,6,4,5,4]

def findRepeating(a):
    slow=a[0]+1
    fast=a[0]+1

    slow=a[slow]+1
    fast=a[a[fast]]+1
    while slow!=fast:
        slow=a[slow]+1
        fast=a[a[fast]]+1

    slow=a[0]

    while slow!=fast:
        slow=a[slow]+1
        fast=a[fast]+1

    return a[slow]

print(findRepeating(a))
'''

'''
Minimize the maximum pages read by a student. Only contiguous books can be read and partial reading not allowed

a=[10,20,10,30]
k=2

def minMaxPagesBook(k,a):
    i=0
    max=a[0]
    sum=0
    while i<len(a):
        sum+=a[i]
        if max<a[i]:
            max=a[i]
        i+=1


    p=max
    q=sum

    ans=None
    while p<=q:
        mid=(p+q)//2
        count=1
        i=0
        sum=0
        while i<len(a):
            if sum+a[i]<=mid:
                sum+=a[i]
            else:
                count+=1
                sum=a[i]

            i+=1

        if count<=k:
            ans=mid
            q=mid-1
        else:
            p=mid+1

    return ans


print(minMaxPagesBook(2,a))
'''