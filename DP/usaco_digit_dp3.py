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
        m,d = lii()
        a = si()
        b = si()
        mod  = 10**9+7

        n = len(b)
        while len(a)<n:a ='0'+a
        
        # dp[i][rem][tightL][tightR] : 
        # count of magic numbers starting of length i with reminder rem
        dp = [[[0]*2 for _ in range(2)] for _ in range(m)]
        dp[0][1][1] = 1

        for i in range(1,n+1):
            new_dp = [[[0]*2 for _ in range(2)] for _ in range(m)]
            for rem in range(m):
                for tightL in [0,1]:
                    for tightR in [0,1]:
                        lower = int(a[i-1]) if tightL else 0
                        upper = int(b[i-1]) if tightR else 9
                        
                        ans = 0
                        for digit in range(lower,upper+1):
                            if(i%2==0 and digit!=d):continue
                            if(i%2==1 and digit==d):continue
                            new_rem = (10*rem+digit)%m
                            new_tightL = tightL&(digit==lower)
                            new_tightR = tightR&(digit==upper)

                            new_dp[new_rem][new_tightL][new_tightR]+=dp[rem][tightL][tightR]
                            new_dp[new_rem][new_tightL][new_tightR]%=mod
            dp = new_dp
        
        ans = 0
        for tightL in [0,1]:
            for tightR in [0,1]:
                ans+=dp[0][tightL][tightR]
                ans%=mod
        return ans

if __name__ == "__main__":
    # fac = factorial(n=2*(10**5)+5,mod=10**9+7)
    # yes,no = "YES","NO"
    # seed = random.randint(0,10**9+7)
    for _ in range(ii()):
        ans = Solution().run()
        print(ans)