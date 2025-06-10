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

        def solve(arr):
            n = len(arr)
            max_sum = curr1 = curr2 = 0
            max_prefix = min_prefix = 0
            for i in range(n):
                curr1+=arr[i]
                curr2+=arr[i]
                if(curr1<0):curr1 = 0
                max_sum = max(max_sum,curr1)
                max_prefix = max(max_prefix,curr2)
                min_prefix = min(min_prefix,curr2)
            return max_sum,max_prefix,min_prefix

        ind = -1
        for i in range(n):
            if(arr[i]!=1 and arr[i]!=-1):
                ind = i
                break
        
        if(ind==-1):
            maxi = solve(arr)[0]
            mini = -solve([-num for num in arr])[0]
            ans = list(range(mini,maxi+1))
            print(len(ans))
            print(*ans)
            return

        maxi1,max_suf,min_suf = solve(arr[:ind][::-1])
        mini1 = -solve([-x for x in arr[:ind]])[0]

        maxi2,max_pref,min_pref = solve(arr[ind+1:])
        mini2 = -solve([-x for x in arr[ind+1:]])[0]

        ans = list(range(mini1,maxi1+1))
        ans.extend(list(range(mini2,maxi2+1)))
        ans.extend(list(range(arr[ind]+min_suf+min_pref,arr[ind]+max_suf+max_pref+1)))
        ans = list(set(ans))

        print(len(ans))
        print(*sorted(ans))

if __name__ == "__main__":
    # fac = factorial(n=2*(10**5)+5,mod=10**9+7)
    # yes,no = "YES","NO"
    # seed = random.randint(0,10**9+7)
    for _ in range(ii()):
        ans = Solution().run()