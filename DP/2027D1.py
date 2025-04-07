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
        n,m = lii()
        a = lii()
        b = lii()

        # dp[i][j]: min cost to make a[0 to i] empty using b[0 to j]
        # transition: dp[i][j] = m-j+min(dp[ind][j],dp[ind][j-1])
        # final dp[n-1][m-1]
        
        def bsIndex(nums,target):
            # works like bisect.left
            # if target is lesser than smallest then index=0
            # if target is larger than largest  then index=n
            low,high = 0,len(nums)-1
            while(low<=high):
                mid = (low+high)>>1
                if(nums[mid]>=target):high = mid-1
                else:low = mid+1
            return low
        
        psum = [a[0]]
        for i in range(1,n):psum.append(psum[-1]+a[i])
        
        dp = [[10**9]*(m) for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if(j>0):dp[i][j] = dp[i][j-1] 
                if(psum[i]<=b[j]):
                    dp[i][j] = m-(j+1)
                    continue
                
                ind = bsIndex(psum,psum[i]-b[j])
                if(ind<i):dp[i][j] = min(dp[i][j],(m-(j+1))+ dp[ind][j])
                
        ans = dp[n-1][m-1]
        return ans if ans<10**9 else -1
        

if __name__ == "__main__":
    # fac = factorial(n=2*(10**5)+5,mod=10**9+7)
    # yes,no = "YES","NO"
    seed = random.randint(0,10**9+7)
    for _ in range(ii()):
        ans = Solution().run()
        print(ans)