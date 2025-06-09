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

        # dp[i][j] - min operations to cover upto row i with state 
        # j:0 - zero 2*2 tiles placed in row i
        # j:1 - left 2*2 tile placed in row i
        # j:2 - right 2*2 tile placed in row i
        # j:3 - both 2*2 tile placed in row i

        dp = [[10**10]*4 for _ in range(n)]
        dp[0][0] = 0+(arr[0]>0)
        if(arr[0]<=2):dp[0][1] = 1
        if(arr[0]<=4):dp[0][3] = 2

        for i in range(1,n):
            # ope 2
            dp[i][0] = dp[i-1][0]+(arr[i]>0)
            
            # ope 1
            if(arr[i]<=2):
                dp[i][0] = min(dp[i][0],dp[i-1][1],dp[i-1][3])
                dp[i][1] = min(dp[i][1],dp[i-1][0]+1,dp[i-1][2]+1)
            
            elif(arr[i]<=4):
                dp[i][0] = min(dp[i][0],dp[i-1][3])
                dp[i][1] = min(dp[i][1],dp[i-1][2]+1)
                dp[i][2] = min(dp[i][2],dp[i-1][1]+1)
                dp[i][3] = min(dp[i][3],dp[i-1][0]+2)
            
        return dp[n-1][0]

if __name__ == "__main__":
    # fac = factorial(n=2*(10**5)+5,mod=10**9+7)
    # yes,no = "YES","NO"
    # seed = random.randint(0,10**9+7)
    for _ in range(ii()):
        ans = Solution().run()
        print(ans)