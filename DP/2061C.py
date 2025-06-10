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
        n = ii()
        arr = lii()
        mod = 998_244_353

        dp = [[0]*2 for _ in range(n)]
        # dp[i][0]: no of configuration with H at i
        # dp[i][1]: no of configuration with L at i

        if(arr[0]==0):dp[0][0] = 1
        dp[0][1] = 1
        
        
        for i in range(1,n):
            # i:H, i-1:H
            if(arr[i]==arr[i-1]):
                dp[i][0]+=dp[i-1][0]
                dp[i][0]%=mod

            # i:H, i-1:L, check i-2==H
            if(arr[i]==1+(arr[i-2] if i-2>=0 else 0)):
                dp[i][0]+=dp[i-1][1]

                dp[i][0]%=mod
            
            # i:L,i-1==H
            dp[i][1]+=dp[i-1][0]
            dp[i][1]%=mod
        
        return (dp[n-1][0]+dp[n-1][1])%mod

if __name__ == "__main__":
    # fac = factorial(n=2*(10**5)+5,mod=10**9+7)
    # yes,no = "YES","NO"
    # seed = random.randint(0,10**9+7)
    for _ in range(ii()):
        ans = Solution().run()
        print(ans)