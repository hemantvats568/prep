'''
largest element in the array
a=[2,2,922,2,2,222]

def findMax(a):
    max=a[0]
    for i in range(len(a)):
        if max<a[i]:
            max=a[i]
    return max

print(findMax(a))
'''

'''
Second largest element in an array
a=[2,2,2,2,2,2]

def secondLargest(a):
    lind=0
    slind=-1

    for i in range(len(a)):
        if a[lind] < a[i]:
            slind = lind
            lind = i
        elif a[slind] < a[i] and a[i] <= a[lind]:
            slind = i
    if slind==-1:
        print("no second largest element found")
        return
    print(a[slind])

secondLargest(a)
'''

'''
Check if an arrary is sorted
a=[1,1,1,2,3,0]

def checkSort(a):
    for i in range(len(a)-1):
        if a[i]>a[i+1]:
            print("False")
            return
    print ("True")

checkSort(a)
'''

'''
Reverse an array
a=[1,5,1,2,3]
def revArr(a):
    i=0
    l=len(a)-1
    while i<=l:
        a[i],a[l]=a[l],a[i]
        i+=1
        l-=1
    return a

print(revArr(a))
'''

'''
Remove duplicates from a sorted array
a=[1,1,1,2,2,3,3,3,4]

def remDup(a):
    currDist=0
    i=1
    if len(a)==0:
        print ("0 distinct")
        return

    while i<len(a):
        if a[i]==a[currDist]:
            i+=1
        else:
            a[i],a[currDist+1]=a[currDist+1],a[i]
            currDist+=1
            i+=1
    return a[:currDist+1]

print(remDup(a))
'''

'''
Move zeroes to end
a=[8,5,0,10,0,8]

def moveZero(a):
    i=0
    currNonZero=-1

    while i<len(a):
        if a[i]==0:
            i+=1
        elif a[i]!=0:
            a[currNonZero+1],a[i]=a[i],a[currNonZero+1]
            currNonZero+=1
            i+=1
    return a

print(moveZero(a))
'''

'''
Left rotate array by 1

a=[1,1,2,5,4,2]

def leftRotate(a):
    if len(a)<=1:
        return a
    return a[1:] + [a[0]]
print(leftRotate(a))
'''

'''
Left rotate an arrary by D places
a=[8,5,0,10,0,8]

def revArr(a):
    i=0
    e=len(a)-1
    while i<=e:
        a[i],a[e]=a[e],a[i]
        i+=1
        e-=1
    return a

def leftRotate(a,d):
    return revArr(revArr(a[:d])+revArr(a[d:]))

print(leftRotate(a,0))
'''

'''
Find leaders in an array
a=[11,5,6,10,8,8]
def leader(a):
    i=len(a)-1
    currMax=a[i]
    while i>=0:
        if i==(len(a)-1):
            print(a[i])
            i-=1
        elif a[i]>currMax:
            print(a[i])
            i-=1
        else:
            i-=1
leader(a)
'''

'''
Maximum difference between a[j]-a[i] such that j > i.
a=[3,2,1]

def maxDiffji(a):
    i=1
    minSoFar=a[0]
    maxDiff=a[1]-a[0]
    if len(a)<2:
        return -1
    while i < len(a):
        if a[i]-minSoFar > maxDiff:
            maxDiff=a[i]-minSoFar
        if a[i]<minSoFar:
            minSoFar=a[i]
        i+=1
    return maxDiff

print(maxDiffji(a))
'''

'''
Frequencies in sorted array

a=[1,1,1,2,3,4,4,4,4,4,5,5,6,6,6,6,8]

def freq(a):
    count=1
    i=0
    l=len(a)-1
    if len(a)<0:
        return
    while i<len(a)-1:
        if a[i]==a[i+1]:
            count+=1
            i+=1
        elif a[i]<a[i+1]:
            print(a[i],count)
            count=1
            i+=1
    print(a[l],count)

freq(a)
'''

'''
Stock buy and sell
prices=[30,20,10]

def maxProfit(a):
    maxProfit=0
    for i in range(len(a)-1):
        if a[i]<a[i+1]:
            maxProfit+=a[i+1]-a[i]
    return maxProfit

print(maxProfit(prices))
'''

'''
Trapping rain water

a=[5,0,6,2,3]

def maxWater(a):
    lmax=[0]*len(a)
    rmax=[0]*len(a)

    max=a[0]
    for i in range(len(a)):
        if a[i] > max:
            max=a[i]
        lmax[i]=max

    end=len(a)-1
    max=a[end]
    while end>=0:
        if a[end] > max:
            max=a[end]
        rmax[end]=max
        end-=1
    maxWat=0
    for i in range(len(a)):
        if i==0 or i==(len(a)-1):
            continue
        maxWat+=min(lmax[i],rmax[i])-a[i]

    return maxWat

print(maxWater(a))
'''

'''
Max consecutive 1's in binary array
a=[0,0,0,0]

def maxOne(a):
    currMax=0
    max=0
    for i in range(len(a)):
        if a[i]==1:
            currMax+=1
        else:
            currMax=0
        if currMax>max:
            max=currMax
    return max

print(maxOne(a))
'''

'''
Max subarray sum (kadane)

a=[10000,-11,-222,-3,99,-1,1000]

def maxSubSum(a):
    currMax=a[0]
    max=a[0]

    for i in range(1,len(a)):
        currMax+=a[i]
        if currMax < a[i]:
            currMax=a[i]
        if max<currMax:
            max=currMax
    return max

print(maxSubSum(a))
'''

'''
Longest even odd subarray
a=[10,12,14,7,8,5]

def isEven(n):
    if n%2==0:
        return True
    else:
        False

def longestEvenOdd(a):
    currMax=0
    max=0

    for i in range(len(a)-1):
        if isEven(a[i]) != isEven(a[i+1]):
            currMax+=1
        else:
            currMax=0
        if max < currMax:
            max=currMax

        print("num:",a[i],"currMax:",currMax,"max:",max)
    return max+1

print (longestEvenOdd(a))
'''

'''
Maximum circular sum

a=[5,-6,-3,4]

def maxSum(a): #kadanes
    i=1
    e=len(a)-1
    res=a[0]
    currMax=a[0]
    while i<=e:
        currMax+=a[i]
        if currMax<a[i]:
            currMax=a[i]
        if res<currMax:
            res=currMax
        i+=1
    return res

def maxCircSum(a):
    totalSum=0
    for i in range(len(a)):
        totalSum+=a[i]

    simpleMaxSum=maxSum(a)

    for i in range(len(a)):
        a[i]=-a[i]

    minSum=-maxSum(a)
    maxSumCirc = totalSum-minSum

    circularSum=max(simpleMaxSum,maxSumCirc)

    return circularSum

print(maxCircSum(a))
'''

'''
Majority element in the array : if element occurs atleast n/2+1 times where n= number of elements in array
a=[6,8,4,8,8,9,8,8]

def majEle(a):
    count=1
    res=a[0]

    for i in range(1,len(a)):
        if a[i]==res:
            count+=1
        else:
            count-=1
        if count==0:
            count=1
            res=a[i]


    checking=0
    for i in range(len(a)):
        if a[i]==res:
            checking+=1


    if checking>len(a)//2:
        return res
    else:
        return None


print(majEle(a))
'''

'''
Minimum consecutive flips: Given a binary array, we need to flip elements to make all elements same. All consecutive same
numbers can be flipped in one go.

a=[1,0,1,0,0,0,1,0,0,1,1,1,1,0]

# In a binary array the starting digit will be occuring more times than the other digit

def minFlips(a):
    count=0
    fele=a[0]

    for i in range(1,len(a)):
        if a[i]!=fele and a[i]!=a[i-1]:
            count+=1

    return count

print(minFlips(a))
'''

'''
Subarray with given sum in an array:
a=[1,4,20,3,10,6]
gs=39

def subGivenSum(a,gs):
    i=0
    e=0
    l=len(a)-1
    currSum=a[i]
    while e<=l:
        if currSum<gs:
            e+=1
            currSum+=a[e]
        if currSum>gs:
            currSum-=a[i]
            i+=1
        if currSum==gs:
            print(i,e)
            return

print(subGivenSum(a,gs))
'''

'''
Prefix sum: given multiple queries to get sum of elements from l to r getSum(l,r).
a=[6,7,3,55,4,9]

ps=[None]*len(a)

sum=0
for i in range(len(a)):
    sum+=a[i]
    ps[i]=sum

def getSum(l,r):
    if l==0:
        return ps[r]
    return ps[r]-ps[l-1]

print(ps)
print(getSum(0,3))
print(getSum(2,3))
'''

'''
Equilibrium point
a=[3,4,8,-9,20,6]

def eqPoint(a):
    tsum=0
    for i in a:
        tsum+=i

    rsum=tsum-a[0]
    lsum=0

    for i in range(1,len(a)):
        lsum+=a[i-1]
        rsum-=a[i]

        if lsum==rsum:
            return a[i]
    return None

print(eqPoint(a))
'''

'''
Maximum appering element in range:
left=[1,2,4]
right=[4,5,7]
max=100
def maxAppear(l,r,max):
    freq=[0]*max
    pfreq=[0]*max
    for i in range(len(l)):
        freq[left[i]]=1
        freq[right[i]+1]=-1

    max=0
    for j in range(1,len(freq)):
        pfreq[j]=pfreq[j-1]+freq[j]
        if pfreq[max]<pfreq[j]:
            max=j
    return max-1


print(maxAppear(left,right,max))
'''
