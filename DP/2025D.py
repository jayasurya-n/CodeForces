from typing import List,Optional
from collections import deque, defaultdict
import sys, heapq, bisect, random
from math import ceil, floor, gcd, sqrt, log

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

class Solution:
    def run(self):
        n,m = lii()
        arr = lii()
        
        # dp[i][p]: max checks u can pass with 'i' intelligence and 'p' points
        # base: dp[0][0] = 0
        # final: max(dp[k][m] for k in range(m))
        
        # transition:
        # if r==0: for i in range(p+1):dp[i][p] = max(dp[i][p-1],dp[i-1][p-1])
        # if r>0: for i in range(r,p+1) :dp[i][p]+=1
        # if r<0: for j in range(-r,p+1):dp[p-j][p]+=1
        
        dp = [[0]*(m+1) for _ in range(m+1)]
        add = [0]*(m+2)
        
        def sumup(dp,p):
            csum = 0
            for i in range(p+1):
                csum+=add[i]
                dp[i][p]+=csum
            for i in range(m+2):add[i] = 0
        
        p = 0
        for r in arr:
            if(r==0):
                sumup(dp,p)
                p+=1
                for i in range(p+1):
                    if(i>0):dp[i][p] = max(dp[i][p],dp[i-1][p-1])
                    if(i<p):dp[i][p] = max(dp[i][p],dp[i][p-1])
                    
            elif(r>0):
                # for i in range(r,p+1):dp[i][p]+=1
                if(r>p):continue
                add[r]+=1
                add[p+1]-=1
                
            elif r<0: 
                r*=-1
                # for i in range(0,p-r+1):dp[i][p]+=1
                if(r>p):continue
                add[0]+=1
                add[p-r+1]-=1
        
        sumup(dp,p)
        return max(dp[k][m] for k in range(m+1))    

if __name__ == "__main__":
    # fac = factorial(n=2*(10**5)+5,mod=10**9+7)
    # yes,no = "YES","NO"
    # seed = random.randint(0,10**9+7)
    for _ in range(1):
        ans = Solution().run()
        print(ans)