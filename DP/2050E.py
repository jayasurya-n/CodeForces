from typing import List,Optional
from collections import deque, defaultdict
import sys, heapq, bisect, random
from math import ceil, floor, gcd, sqrt, log

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

def factorial(n,mod):
    fac = [1]*n
    for i in range(1,n):
        fac[i] = (fac[i-1]*i)%mod
    return fac

def nCr(n,r,fac,mod):
    if(n<r or n<0 or r<0):return 0
    return fac[n]*pow(fac[r],mod-2,mod)*pow(fac[n-r],mod-2,mod)

class Solution:
    def run(self):
        a,b,c = si(),si(),si()
        la,lb,lc = len(a),len(b),len(c)
        
        # dp[i][j] = min changes in the string  c[1 to i+j-1] forming 
        # from a[1 to i] and b[1 to j] 
        
        # trainsition:dp[i][j]  = 1+min(dp[i-1][j],dp[i][j-1])
        # final: dp[la][lb]
        # base case: 
            # dp[i][0] = 1-(c[0]==a[0])
            # dp[0][j] = 1-(c[0]==b[0])
        
        dp = [[0]*(lb+1) for _ in range(la+1)]
        for i in range(1,la+1):dp[i][0] = dp[i-1][0]+(a[i-1]!=c[i-1])
        for j in range(1,lb+1):dp[0][j] = dp[0][j-1]+(b[j-1]!=c[j-1])
        
        for i in range(1,la+1):
            for j in range(1,lb+1):
                if(a[i-1]==c[i+j-1]):dp[i][j] = dp[i-1][j]
                else:dp[i][j] = 1+dp[i-1][j]
                
                if(b[j-1]==c[i+j-1]):dp[i][j] = min(dp[i][j],dp[i][j-1])
                else:dp[i][j] = min(dp[i][j],1+dp[i][j-1])
        
        # for row in dp:print(row)
        return dp[la][lb]

if __name__ == "__main__":
    # fac = factorial(n=2*(10**5)+5,mod=10**9+7)
    # yes,no = "YES","NO"
    seed = random.randint(0,10**9+7)
    for _ in range(ii()):
        ans = Solution().run()
        print(ans)