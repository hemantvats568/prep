'''
Print all permutations. Given a string, print all permutations of it.
ABC

ABC,      BAC,      CBA     --> Swap fixed index 0 with all indexes including 0 index
ABC,ACB   BAC,BCA   CBA,CAB --> After fixing index 0, swap index 1 with all indexes remaining including 1 index
                            --> return when index reaches 2
'''
'''
str = list(input("Please enter the string: "))
def swap (x,a,b):
    x[a], x[b] = x[b], x[a]
    return x

def permutations(str,fi):
    if fi==(len(str)-1):
        print(str)
        return
    for i in list(range(len(str)))[fi:]:
        swap(str,fi,i)
        permutations(str,fi+1)
        swap(str,i,fi)     # We don't want to make change to the original string as we derive all other strings from it. So we need to swap back.

permutations(str,0)
'''

'''
Subset Sum Problem:
Find all subsets whose sum is equal to the given sum

set = {2,1,9}, sum=11
subsets = {},{2},{1},{9},{2,1},{1,9},{2,9},{2,1,9}

# Not using actual set because indexing makes no sense for sets. Hence using list
# st = list(map(int,input("Please enter space separated numbers of set: ").split(" ")))

#Trying GFG Soln
def subsetsum(st,sum,n):
    if n==0:
        # print(1 if (sum==0) else 0)
        return (1 if (sum==0) else 0)
    # print(subsetsum(st,sum,n-1))
    # print(subsetsum(st,sum-st[n-1],n-1))
    return (subsetsum(st,sum,n-1) + subsetsum(st,sum-st[n-1],n-1))

print(subsetsum([1,3,4],4,3))
'''

'''
Josephus Problem
A circle has N people and Kth person is killed in every turn. The gun gets passed to k+1th person and so on. Find person number that remains in the end
0,1,2,3
(5,3) --> After First iteration 
--> Index 3 becomes new 0 index
--> Index 4 becomes new 1 index
--> Index 0 becomes new 2 index and so on.
Therefore we will use (return ((func(n-1,k)+k)%n))                                    
def joseph(n,k):
    if n==1:
        return 0
    return (joseph(n-1,k)+k)%n

print(joseph(5,3))
'''

'''
Tower of Hanoi
Move n disks from tower a to c using b as auxiliary. Print all steps
To think recursion, think of using solution for n-1 disks and then create solution for n disks. Nth disk is to b the bottommost disk

def toh(n,a,b,c):
    if n==0:
        return print("")
    toh(n-1,a,c,b)
    print(("move disk " + str(n) + " from "+a+" to "+c))
    toh(n-1,b,a,c)

toh(3,"a","b","c")
'''
'''
Generate subsets: Generate all subsets of a set or all subsequences of a string
If we have a solution for n-1 then we have two choices, either to include it or not include it. We start with empty subsequence "" and iterate from there for each element.
Also we have to maintain an index "i" in this case to write the base case. Without this index we won't know when to stop.

def subs(s,i,new):
    if i==len(s):
        print(new)
        return
    subs(s,i+1,new+s[i])
    subs(s,i+1,new)
new = ""
i=0
subs(s,i,new)

Need to find a solution for subset and not sub sequence
'''
'''
Rope cutting problem:
Given a rope of length l, and a set of 3 allowed piece lengths. Find the maximum number of pieces that the rope can be cut into using only those piece sizes

# def maxpieces(l,a,b,c):
#     if l<0:
#         return -1
#     if l==0:
#         return 0
#     res = max(maxpieces(l-a,a,b,c),maxpieces(l-b,a,b,c),maxpieces(l-c,a,b,c))
#     if res<0:
#         return -1
#     else:
#         res = res + 1
#     return res
# 
# print(maxpieces(5,5,2,2))
'''
'''
Sum of digits using recursion

def sumdigit(n):
    if n<=0:
        return 0
    sum = n%10 + sumdigit(n//10)
    return sum
'''

'''
Palindrome check using recursion

def checkpalindrome(st):
    if len(st)==1:
        return True
    if len(st)==2:
        return st[0]==st[1]
    if not (st[0]==st[-1]):
        return False
    checkpalindrome(st[0:-1])
    return True

print(checkpalindrome("abc"))
'''

'''
Sum of first n natural numbers using recursion
def sumnatural(n):
    if n<=0:
        return 0
    return (n + sumnatural(n-1))
'''

'''
Tail recursion: When the last thing that a function does is recursive call. So, when the child recursive call finishes the parent
does not have anything else to do. Modern compilers do tail call elimination. This makes execution faster. EG: Quick sort is tail
recursive whereas merge sort is not.
'''