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

        dp = [[0]*3 for _ in range(n)]
        dp[0] = [1,0,0]

        for i in range(1,n):
            dp[i][0] = dp[i-1][0]+(arr[i]>dp[i-1][0])-(arr[i]<dp[i-1][0])
            dp[i][1] = max(dp[i-1][0],dp[i-1][1])
            dp[i][2] = max(dp[i-1][1]+(arr[i]>dp[i-1][1])-(arr[i]<dp[i-1][1]),
                           dp[i-1][2]+(arr[i]>dp[i-1][2])-(arr[i]<dp[i-1][2]))
        
        return max(dp[n-1][1],dp[n-1][2])

if __name__ == "__main__":
    # fac = factorial(n=2*(10**5)+5,mod=10**9+7)
    # yes,no = "YES","NO"
    # seed = random.randint(0,10**9+7)
    for _ in range(ii()):
        ans = Solution().run()
        print(ans)