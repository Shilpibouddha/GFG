#User function Template for python3
class Solution:

	def convert(self,arr, n):
	    
	    
	    sorted_arr = sorted(arr)

        index_map = {val: i for i, val in enumerate(sorted_arr)}

        for i, val in enumerate(arr):

            arr[i] = index_map[val]




#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.convert(arr, n)
        for x in arr:
            print(x, end=" ")
        print()
        tc -= 1

# } Driver Code Ends