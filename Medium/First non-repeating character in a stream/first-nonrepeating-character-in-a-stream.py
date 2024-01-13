#User function Template for python3
from collections import deque
class Solution:
	def FirstNonRepeating(self, A):
	    que = deque()
		
		freq = dict()
		
		ans = ''
		
		for char in A:
		    if char in freq:
		        freq[char] += 1
		    else:
		        freq[char] = 1
		    
		    if freq[char] == 1:
		        que.append(char)
	        
	        while que and freq[que[0]] > 1:
	            que.popleft()
	        
	        if not que:
	            ans += '#'
	        else:
	            ans += que[0]
        return ans


#{ 
 # Driver Code Starts

#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		A = input()
		ob = Solution()
		ans = ob.FirstNonRepeating(A)
		print(ans)

# } Driver Code Ends