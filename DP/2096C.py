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
        # n = ii()
        # heights = []
        # for _ in range(n):
        #     heights.append(lii())
        
        # a = lii()
        # b = lii()

        # def solve(heights,a):
        #     equal = [-1]
        #     upper = [-1]
        #     lower = [-1]

        #     for i in range(1,n):
        #         same = diff1 = diff2 = False
        #         for j in range(n):
        #             if(heights[i][j]==heights[i-1][j]):same = True
        #             if(heights[i][j]==heights[i-1][j]+1):diff2 = True
        #             if(heights[i][j]==heights[i-1][j]-1):diff1 = True
                
        #         equal.append(same)
        #         upper.append(diff2)
        #         lower.append(diff1)

        #     dp = [[10**15]*2 for _ in range(n)]
        #     dp[0] = [0,a[0]]

        #     for i in range(1,n):
        #         if(dp[i-1][0]!=10**15):
        #             if(not equal[i]):dp[i][0] = min(dp[i][0],dp[i-1][0])
        #             if(not lower[i]):dp[i][1] = min(dp[i][1],dp[i-1][0]+a[i])
                
        #         if(dp[i-1][1]!=10**15):
        #             if(not upper[i]):dp[i][0] = min(dp[i][0],dp[i-1][1])
        #             if(not equal[i]):dp[i][1] = min(dp[i][1],dp[i-1][1]+a[i])

        #     return min(dp[n-1][0],dp[n-1][1])
    
        # cost1 = solve(heights,a)

        # for i in range(n):
        #     for j in range(i):
        #         heights[i][j],heights[j][i] = heights[j][i],heights[i][j]
        
        # cost2 = solve(heights,b)

        # if(cost1==10**15 or cost2==10**15):return -1
        # return cost1+cost2

        n = ii()
        heights = []
        for _ in range(n):
            heights.append(lii())
        
        a = lii()
        b = lii()

        def solve(heights,a):
            dp = [[10**15]*2 for _ in range(n)]
            dp[0] = [0,a[0]]

            for i in range(1,n):
                for x in range(2):
                    for y in range(2):
                        ok = True
                        for j in range(n):
                            ok&=(heights[i][j]+x!=heights[i-1][j]+y)
                        
                        if(not ok or dp[i-1][y]==10**15):continue
                        dp[i][x] = min(dp[i][x],dp[i-1][y]+(a[i] if x==1 else 0))

            return min(dp[n-1])
    
        cost1 = solve(heights,a)

        for i in range(n):
            for j in range(i):
                heights[i][j],heights[j][i] = heights[j][i],heights[i][j]
        
        cost2 = solve(heights,b)

        if(cost1==10**15 or cost2==10**15):return -1
        return cost1+cost2

if __name__ == "__main__":
    # fac = factorial(n=2*(10**5)+5,mod=10**9+7)
    # yes,no = "YES","NO"
    # seed = random.randint(0,10**9+7)
    for _ in range(ii()):
        ans = Solution().run()
        print(ans)