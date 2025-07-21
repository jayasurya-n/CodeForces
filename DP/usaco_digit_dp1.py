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
        a,b = lii()
        b = str(b)
        n = len(b)
        candidates = [a,int(b)]

        for i in range(n):
            if(b[i]=='0'):continue
            prefix = b[:i]
            digit = str(int(b[i])-1)
            suffix = '9'*(n-i-1)
            candidate = int(prefix+digit+suffix)
            if(candidate>a):candidates.append(candidate)
        
        def find_digit_product(num):
            ans = 1
            while num>0:
                ans*=num%10
                num//=10
            return ans

        candidates.sort(key=lambda x:find_digit_product(x),reverse=True)
        return candidates[0]

if __name__ == "__main__":
    # fac = factorial(n=2*(10**5)+5,mod=10**9+7)
    # yes,no = "YES","NO"
    # seed = random.randint(0,10**9+7)
    for _ in range(1):
        ans = Solution().run()
        print(ans)