from typing import List,Optional
from collections import deque, defaultdict
import sys, heapq, bisect, random
from math import ceil, floor, gcd, sqrt, log

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

class DisjointSet:
    def __init__(self,n):
        self.size = [1]*(n+1)
        self.parent = list(range(n+1))

    def findUltimateParent(self,u):
        if(u==self.parent[u]):return u
        self.parent[u] = self.findUltimateParent(self.parent[u])
        return self.parent[u]

    def unionbySize(self,u,v):
        rootu = self.findUltimateParent(u)
        rootv = self.findUltimateParent(v)
        if(rootu==rootv):return

        size_u = self.size[rootu]
        size_v = self.size[rootv]

        if(size_u < size_v):
            self.parent[rootu] = rootv
            self.size[rootv]+=size_u
        else:
            self.parent[rootv] = rootu
            self.size[rootu]+=size_v

class Solution:
    def run(self):
        n,m = lii()
        arr = [[0]*11 for _ in range(n+1)]
        for _ in range(m):
            a,d,k = lii() 
            arr[a][d] = max(arr[a][d],k)
        
        ds = DisjointSet(n+1)
        
        for d in range(1,11):
            for i in range(1,n):
                steps = arr[i][d] 
                if(steps==0):continue
                
                j = i
                while(j+d<=n and steps>0):
                    ds.unionbySize(j,j+d)
                    arr[j][d] = 0
                    steps-=1
                    steps = max(steps,arr[j+d][d])
                    j+=d
        
        ans = 0
        for i in range(1,n+1):
            if(ds.findUltimateParent(i)==i):ans+=1
        return ans

if __name__ == "__main__":
    # fac = factorial(n=2*(10**5)+5,mod=10**9+7)
    # yes,no = "YES","NO"
    # seed = random.randint(0,10**9+7)
    for _ in range(ii()):
        ans = Solution().run()
        print(ans)