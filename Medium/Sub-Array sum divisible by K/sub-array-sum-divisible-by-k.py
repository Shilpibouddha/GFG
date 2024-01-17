class Solution:
    def subCount(self,arr, n, k):
        count = 0
        cur_s = 0
        d = {0:1}
        for i in range(n):
            cur_s += a[i]
            r = cur_s % k
            if r in d:
                count += d[r]
                d[r] += 1
            else:
                d[r] = 1
        return count
        # Your code goes here


#{ 
 # Driver Code Starts
if __name__ == '__main__': 
    
    t=int(input())
    for _ in range(0,t):
        l=list(map(int,input().split()))
        n=l[0]
        k=l[1]
        a = list(map(int,input().split()))
        ob = Solution()
        print(ob.subCount(a,n,k))
# } Driver Code Ends