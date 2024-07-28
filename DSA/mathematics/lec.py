'''
Count digits in a number
def countdigits(n):
    count=0
    if n<0:
        n=n*-1
    if n<1:
        return 0
    while n!=0:
        count+=1
        n=n//10
    return count
'''
'''
Palindrome number: Check if a number is palindrome or not
def checkpalindrome(n):
    new = 0
    extra = n
    while extra>0:
        new = extra%10 + new*10
        extra = extra//10
    if new==n:
        return True
    return False
'''
'''
Factorial of a number.
For factorial loop is better than recursion as recursion has more space complexity whereas time complexity is same in both approach.
def factorial(n):
    if n<=0:
        return 1
    res=1
    while n>0:
        res=res*n
        n=n-1
    return res
'''
'''
Count trailing zeros in factorial of n.
If we are able to count number of 5s that will occur in factorial of a number we can get the number of zeroes. So we first
count number of 5s then we take into account number of 5s from numbers like 25 and 125 and so on.
def countfactzeros(n):
    count=0
    while n>0:
        count=count+n//5
        n=n//5
    return count
'''
'''
HCF of two numbers: We can use euclidean algorithm which says hcf(a,b) = hcf(a,b,a-b = hcf(a,b,a%b) if a>b.

def hcf(a,b):
    if b==0:
        return a
    else:
        return hcf(b,a%b)
'''
'''
LCM of two numbers: Same as above find gcd and use lcm*hcf= product of numbers
'''

'''
Check for prime: Check if a number is prime or not. Keep in mind the optimization below

def checkprime(n):
    if n<=1:
        return False
    if n==2 or n==3:
        return True
    if n%2==0 or n%3==0:
        return False
    i=5
    while i*i<=n:
        if n%i==0 or n%(i+2)==0:
            return False
        i=i+6
    return True

print(checkprime(int(input("Please pass number: "))))
'''

'''
Find all prime factors. Just like check prime code we will just run the loop till sqrt n and while the number is divisible
we repeatedly divide by the factor that we find along the way and keep a base case if number is prime. No need to check if
divisor is prime as when we start from 2 all factors will be consumed already, so no composite factors will be found.

def allprimefactors(n):
    if n<=1:
        return None
    i=2
    while i*i<=n:
        while n%i==0:
            print(i,end=" ")
            n=n//i
        i+=1
    if n>1:
        print(n)
    finish="all prime factors printed above"
    return finish
'''

'''
Print all factors in sorted order: Only use the basic fact that factors appear in pair such that one is less than sqrt(n)
and other is more than sqrt(n). We run the loop twice once from 1 to sqrt(n) and then from sqrt(n) to 1 without resetting
the index.

def allfactors(n):
    if n<1:
        return None
    print(1)
    i=2
    while i*i<=n:
        if n%i==0:
            print(i)
        i+=1
    i-=1
    while i>0:
        if n%i==0:
            print(n//i)
        i-=1
'''
'''
Sieve of eratosthenes: Print all prime numbers less than a number n.
We initialize an array with all indexes more than and equal to 2 as True. Then for all prime numbers
def isPrime(n):
    if n==0 or n==1:
        return False
    if n==2 or n==3:
        return True
    if n%2==0 or n%3==0:
        return False
    i=5
    while i*i<=n:
        if n%i==0 or n%(i+2)==0:
            return False
        i+=6
    return True

def sieve(n):
    sieve=[True]*(n+1)
    i=2
    while i*i<=n:
        if isPrime(i):
            j=2*i
            while j<=n:
                sieve[j]=False
                j+=i
        i+=1
    k=2
    while k<=n:
        if sieve[k]:
            print(k,end=" ")
        k+=1
'''
'''
Power of a number: pow(x,n). 
There are two solutions. One is recursive O(log(n)) and O(log(n)) auxiliary space as well.
def recpow(x,n):
    if n<0:
        return None
    if x==0:
        return 0
    if n==0:
        return 1
    temp = recpow(x,n//2)
    temp = temp*temp
    if n%2==0:
        return temp
    else:
        return temp*x
        
Another solution is iterative where we can get O(1) auxiliary space and same time complexity.
In iterative power solution. We focus on the power n. The idea is that n can be converted to bits for example x^5. 5 can
be written as 101 in binary and then we can iterate over each bit and if it is not zero then we multiply is by suitable number.
To get the suitable number in each iteration we make the number as x^2. So for first bit number is 1, then in second iteration
the number becomes x^2 and in third x^4 and so on.

def iterpow(x,n):
    res=1
    if n<0:
        return None
    if x==0:
        return 0
    if n==0:
        return 1
    while n>0:
        if n%2==0:
            pass
        else:
            res=res*x
        x=x*x
        n=n//2
    return res
'''
