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
        l,r = list(map(str,sorted(lii())))
        n = len(r)
        while len(l)<n:l = '0'+l

        def solve(i,tL,tR):
            if(n%2==0 and i==n//2):return 1
            if(n%2==1 and i==(n+1)//2):return 1

            if((i,tL,tR) in dp):return dp[(i,tL,tR)]

            upper = min(int(r[i]),int(r[n-i-1])) if tR else 9
            lower = min(int(l[i]),int(l[n-i-1])) if tL else 0

            ans = 0
            for digit in range(lower,upper+1):
                nextL = tL&(digit==lower)
                nextR = tR&(digit==upper) 
                ans+=solve(i+1,nextL,nextR)
            
            dp[(i,tL,tR)] = ans
            return ans


        dp = {}
        return solve(0,1,1)

        
        

if __name__ == "__main__":
    # fac = factorial(n=2*(10**5)+5,mod=10**9+7)
    # yes,no = "YES","NO"
    # seed = random.randint(0,10**9+7)
    for _ in range(ii()):
        ans = Solution().run()
        print(ans)