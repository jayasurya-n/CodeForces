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
        arr = [list(si()),list(si())] 

        for i in range(2):
            for j in range(n):
                if(arr[i][j]=='A'):arr[i][j]=1
                else:arr[i][j] = 0

        dp = [[0]*3 for _ in range(n)]
        # dp[i][j] all the houses are paired upto i-1 and
        # j:0 both houses at i are paired
        # j:1 top house at i is paired
        # j:2 bottom  house at i is paired

        # final: dp[n-1][0]
        
        def vote(a,b,c):
            return a+b+c>=2

        for i in range(n):
            if(i>=2):
                dp[i][0] = max(dp[i][0],(dp[i-3][0] if i>=3 else 0)+
                                 vote(arr[0][i-2],arr[0][i-1],arr[0][i])+
                                 vote(arr[1][i-2],arr[1][i-1],arr[1][i]))
            if(i>=1):
                dp[i][0] = max(dp[i][0],(dp[i-1][1] if i>=1 else 0) + 
                            vote(arr[1][i-1],arr[0][i],arr[1][i]))

                dp[i][0] = max(dp[i][0],(dp[i-1][2] if i>=1 else 0) + 
                          vote(arr[0][i-1],arr[0][i],arr[1][i]))
            
            if(i>=2):
                dp[i][1] = max(dp[i][1],(dp[i-3][1] if i>=3 else 0)+
                                 vote(arr[1][i-3],arr[1][i-2],arr[1][i-1])+
                                 vote(arr[0][i-2],arr[0][i-1],arr[0][i]))
            
            if(i>=1):
                dp[i][1] = max(dp[i][1],(dp[i-2][0] if i>=2 else 0) + 
                            vote(arr[0][i-1],arr[1][i-1],arr[0][i]))
            
            if(i>=2):
                dp[i][2] = max(dp[i][2],(dp[i-3][2] if i>=3 else 0)+
                                 vote(arr[0][i-3],arr[0][i-2],arr[0][i-1])+
                                 vote(arr[1][i-2],arr[1][i-1],arr[1][i]))
            
            if(i>=1):
                dp[i][2] = max(dp[i][2],(dp[i-2][0] if i>=2 else 0) + 
                            vote(arr[0][i-1],arr[1][i-1],arr[1][i]))

        return dp[n-1][0]


if __name__ == "__main__":
    # fac = factorial(n=2*(10**5)+5,mod=10**9+7)
    # yes,no = "YES","NO"
    # seed = random.randint(0,10**9+7)
    for _ in range(ii()):
        ans = Solution().run()
        print(ans)