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
        # n,m,v = lii()
        # arr = lii()

        # def solve(arr,v):
        #     prefix = [0]*(n+1)
        #     curr = 0
        #     for i in range(1,n+1):
        #         prefix[i] = prefix[i-1]
        #         curr+=arr[i-1]
        #         if(curr>=v):
        #             prefix[i] = prefix[i-1]+1
        #             curr = 0
            
        #     return prefix

        # prefix = solve(arr,v)
        # suffix = solve(arr[::-1],v)

        # psum = [0]*(n+1)
        # for i in range(1,n+1):
        #     psum[i] = psum[i-1]+arr[i-1]

        # ans = -1
        # for i in range(1,n+1):
        #     count = suffix[n-i]
        #     rem = m-count
        #     ind = bisect.bisect_left(prefix,rem)
        #     if(ind<=i):
        #         ans = max(ans,psum[i]-psum[ind])
        # return ans


        n,m,v = lii()
        arr = lii()

        def solve(arr,v):
            prefix = [0]*(n+1)
            curr = 0
            for i in range(1,n+1):
                prefix[i] = prefix[i-1]
                curr+=arr[i-1]
                if(curr>=v):
                    prefix[i] = prefix[i-1]+1
                    curr = 0
            
            return prefix

        prefix = solve(arr,v)
        suffix = solve(arr[::-1],v)[::-1]

        psum = [0]*(n+1)
        for i in range(1,n+1):
            psum[i] = psum[i-1]+arr[i-1]

        ans = -1
        j = 0
        for i in range(n+1):
            while(j<n and prefix[i]+suffix[j+1]>=m):j+=1
            if(prefix[i]+suffix[j]>=m):
                ans = max(ans,psum[j]-psum[i])
        return ans

if __name__ == "__main__":
    # fac = factorial(n=2*(10**5)+5,mod=10**9+7)
    # yes,no = "YES","NO"
    # seed = random.randint(0,10**9+7)
    for _ in range(ii()):
        ans = Solution().run()
        print(ans)