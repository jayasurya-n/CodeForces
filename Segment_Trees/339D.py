import math, heapq, bisect, random, sys
from collections import deque, defaultdict

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))
modinv = lambda a,mod:pow(a,mod-2,mod)

from types import GeneratorType
def bootstrap(f, stack=[]):
    def wrappedfunc(*args,**kwargs):
        if stack:return f(*args,**kwargs)
        else:
            to = f(*args,**kwargs)
            while True:
                if isinstance(to, GeneratorType):
                    stack.append(to)
                    to = next(to)
                else:
                    stack.pop()
                    if not stack:break
                    to = stack[-1].send(to)
            return to
    return wrappedfunc

class SegmentTree:
    def __init__(self,arr,n,p):
        self.seg = [0]*4*n
        self.build(0,0,n-1,arr,orr=p%2)
    
    @bootstrap
    def build(self,node,low,high,arr,orr):
        if(low==high):
            self.seg[node] = arr[low]
            yield
        
        mid = (low+high)>>1
        yield self.build(2*node+1,low,mid,arr,1-orr)
        yield self.build(2*node+2,mid+1,high,arr,1-orr)
        if(orr):self.seg[node] = self.seg[2*node+1]|self.seg[2*node+2]   
        else:self.seg[node] = self.seg[2*node+1]^self.seg[2*node+2] 
        yield  

    @bootstrap
    def update(self,node,low,high,pos,val,orr):
        if(low==high):
            self.seg[node]=val
            yield
        
        mid = (low+high)//2
        if(pos<=mid):yield self.update(2*node+1,low,mid,pos,val,1-orr)
        else:yield self.update(2*node+2,mid+1,high,pos,val,1-orr)
        if(orr):self.seg[node] = self.seg[2*node+1]|self.seg[2*node+2]   
        else:self.seg[node] = self.seg[2*node+1]^self.seg[2*node+2]   
        yield

class Solution:
    def run(self):
        n,m = lii()
        arr = lii()

        length = 1<<n
        seg_tree = SegmentTree(arr,length,n)
        for _ in range(m):
            pos,val = lii()
            seg_tree.update(0,0,length-1,pos-1,val,n%2)
            print(seg_tree.seg[0])


if __name__ == "__main__":
    # yes,no = "YES","NO"
    # seed = random.randint(0,10**9+7)
    for _ in range(1):
        ans = Solution().run()