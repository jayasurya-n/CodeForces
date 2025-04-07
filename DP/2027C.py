from typing import List,Optional
from collections import deque, defaultdict
import sys, heapq, bisect, random
from math import ceil, floor, gcd, sqrt, log

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

def factorial(n,mod):
    fac = [1]*n
    for i in range(1,n):
        fac[i] = (fac[i-1]*i)%mod
    return fac

def nCr(n,r,fac,mod):
    if(n<r or n<0 or r<0):return 0
    return fac[n]*pow(fac[r],mod-2,mod)*pow(fac[n-r],mod-2,mod)

class Solution:
    def run(self):
        n = ii()
        arr = lii()
        
        adj = defaultdict(list)
        for i,num in enumerate(arr):
            u = i+num
            v = u+i
            adj[u^seed].append(v)
        
        self.ans = n
        visited = set()
        visited.add(n^seed)
        q = deque([n^seed])
        
        while q:
            u = q.popleft()
            self.ans = max(self.ans,u^seed)
            
            for v in adj[u]:
                v^=seed
                if(v in visited):continue
                visited.add(v)
                q.append(v)
        return self.ans

if __name__ == "__main__":
    # fac = factorial(n=2*(10**5)+5,mod=10**9+7)
    # yes,no = "YES","NO"
    seed = random.randint(0,10**9+7)
    for _ in range(ii()):
        ans = Solution().run()
        print(ans)