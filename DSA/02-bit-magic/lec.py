'''
Check if kth bit is set or not for a number n

def checksetbit(n,k):
    return False if ((n&(1<<k))==0) else True
'''

'''
Count set bits in number n
n & n-1 removes all the trailing zeros and makes the last set bit 0. This is known as brian kernighan's algorithm.
def countsetbit(n):
    count=0
    while n!=0:
        count+=1
        n=n&(n-1)
    return count

Another better approach is to preprocess a 2^8 size table and initialize that table with count of set bits in numbers from 
0 to 255. Then use this table to find set bits in a number. This will give O(1) time complexity.
Effectively the table has number of set bits in all numbers from 1 to 255. And with 255 will keep the last 8 set bits intact and remove all previous bits. Hence helps in checking number of set bits in last 8 bits.
table = [0]*256
table[0]=0
for i in range(1,256):
    table[i] = table[i&(i-1)] + 1 # Basicallly to fill the table when we do table[i&(i-1)] we are removing one set bit from the number and picking a value from another prefilled index values which is smaller than requried current index and adding one since one idex is removed.
def countsetbit(n):
    return table[n&255] + table[(n>>8)&255] + table[(n>>16)&255] + table[(n>>24)&255]
'''
'''
Check if a number is a power of 2 or not. Power of two will only have one set bit and running brian kernighan's once is enough.
def ispowtwo(n):
    if n<=0:
        return False
    return (n&(n-1)==0)
'''
'''
One odd occuring. There is an array of numbers and that array has elements in a way that all numbers are present even number of times except on element which is present odd number of times. We have to find that number
We will xor all elements. XOR of a number with itself will make the number 0 and xor with 0 gives the number itself. So only remaining number will be the one having odd count.
def findoddoccur(n):
    res=n[0]
    for i in n[1:]:
        res=res^i
    return res
'''

'''
Two odd occuring: All elements in an array occur even number of times and two elements occur odd number of times.
x&(~(x-1)) gives a number which has only last set bit of x.
We will xor all elements. This xor will be an xor of two odd occuring elements.Only one of the two numbers will have 
the last set bit same as the last set bit of the xor as xor would have unset it if both numbers had it set.and generate
 a number k which will have only last set bit from the xor of all elements. Now we will take xor of only those numbers 
 that has last set bit as k and another xor of numbers that don't have last set bit as k. This will result in two numbers.

def twooddoccur(n):
    res = n[0]
    for i in n[1:]:
        res=res^i
    k = res&(~(res-1))
    res1=0
    res2=0
    for i in n:
        if k&i==0:
            res1=res1^i
        else:
            res2=res2^i

    return [res1,res2]
'''
'''
Print all subsets of a string (Powerset). We know that a string of size n has x=2^n-1 subsets. We create a list of size
x=2^n-1 and then for each value of index of i we iterate over binary representation of index and print the character if 
binary digit is 1.

def powset(s):
    n = len(s)
    x = (1<<n)
    for i in range(x):
        for j in range(n):
            if (i & (1<<j)!=0):
                print(s[j],end="")
        print("")
        final = "all sets have been printed above"
    return final
'''
