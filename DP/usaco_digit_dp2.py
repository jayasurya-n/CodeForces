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
        a,b = lii()
        a = list(map(int,str(a)))
        b = list(map(int,str(b)))
        n = len(b)
        

        def solve(ind,tightL,tightR):
            if(ind==len(b)):return [1,0]

            if(dp[ind][tightL][tightR]!=-1):
                return dp[ind][tightL][tightR]
            
            lower = a[ind-(n-len(a))] if ind>=n-len(a) and tightL else 0
            upper = b[ind] if tightR else 9

            cnt = tsum = 0
            for digit in range(lower,upper+1):
                next_tightL = tightL&(digit==lower)
                next_tightR = tightR&(digit==upper)

                cnt_sub,tsum_sub = solve(ind+1,next_tightL,next_tightR)

                tsum+=tsum_sub+cnt_sub*digit
                cnt+=cnt_sub

            dp[ind][tightL][tightR] = [cnt,tsum]
            return dp[ind][tightL][tightR]

        dp = [[[-1]*2 for _ in range(2)] for _ in range(n)]
        return solve(0,1,1)[1]
        

if __name__ == "__main__":
    # fac = factorial(n=2*(10**5)+5,mod=10**9+7)
    # yes,no = "YES","NO"
    # seed = random.randint(0,10**9+7)
    for _ in range(ii()):
        ans = Solution().run()
        print(ans)