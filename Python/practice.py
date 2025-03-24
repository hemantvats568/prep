n=10
def countzeros(n):
    ans=0
    pow=5
    while pow <= n:
        ans+= n//pow
        pow*=5
    return ans

print(countzeros(n))