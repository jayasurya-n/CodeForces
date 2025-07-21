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
        n,x = lii()
        arr = lii()

        arr.reverse()
        psum = [0]*(n+1)
        for i in range(1,n+1):
            psum[i] = psum[i-1]+arr[i-1]

        # dp[i]:number of segments ending at index i 
        dp = [0]*(n+1)
        for i in range(1,n+1):
            ind = bisect.bisect_left(psum,psum[i]-x)
            if(ind>0):dp[i]+=dp[ind-1]+1
        return (n*(n+1))//2-sum(dp)

if __name__ == "__main__":
    # fac = factorial(n=2*(10**5)+5,mod=10**9+7)
    # yes,no = "YES","NO"
    # seed = random.randint(0,10**9+7)
    for _ in range(ii()):
        ans = Solution().run()
        print(ans)