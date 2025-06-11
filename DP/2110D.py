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
        batteries = lii()
        adj = [[] for _ in range(n)]
        for _ in range(m):
            u,v,w = lii()
            adj[u-1].append((v-1,w))
        
        def check(mid):
            dp = [0]*n
            for u in range(n-1):
                if(u>0 and dp[u]==0):continue
                dp[u] = min(dp[u]+batteries[u],mid)

                for v,w in adj[u]:
                    if(w<=dp[u]):
                        dp[v] = max(dp[v],dp[u])

            return dp[n-1]>0

        low,high = 0,10**9
        while(low<=high):
            mid = (low+high)>>1
            if(check(mid)):high = mid-1
            else:low = mid+1
        return low if low<=10**9 else -1

if __name__ == "__main__":
    # fac = factorial(n=2*(10**5)+5,mod=10**9+7)
    # yes,no = "YES","NO"
    # seed = random.randint(0,10**9+7)
    for _ in range(ii()):
        ans = Solution().run()
        print(ans)