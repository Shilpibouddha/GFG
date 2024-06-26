#User function Template for python3
class Solution:
	def maxDotProduct(self, n, m, a, b):
	    dp=[[0]*(n+1) for _ in range(m+1)]
        for y in range(1,m+1):
            for x in range(y,n+1):
                mx=dp[y-1][x-1]+a[x-1]*b[y-1]
                mx=max(mx,dp[y][x-1])
                dp[y][x]=mx
        return dp[-1][-1]

		# code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n,m = input().split()
		n,m = int(n),int(m)
		a = [int(x) for x in input().split()]
		b = [int(x) for x in input().split()]
		ob = Solution()
		ans = ob.maxDotProduct(n,m,a,b)
		print(ans)
# } Driver Code Ends