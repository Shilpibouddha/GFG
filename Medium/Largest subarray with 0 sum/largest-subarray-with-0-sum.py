#Your task is to complete this function
#Your should return the required output
class Solution:
    def maxLen(self, n, arr):
        sum_map = {}
        max_length = 0
        cumulative_sum = 0

        for i in range(n):
            cumulative_sum += arr[i]

            if cumulative_sum == 0:
                max_length = i + 1

            if cumulative_sum in sum_map:
                max_length = max(max_length, i - sum_map[cumulative_sum])
            else:
                sum_map[cumulative_sum] = i

        return max_length



   


#{ 
 # Driver Code Starts
if __name__=='__main__':
    t= int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.maxLen(n ,arr))
# Contributed by: Harshit Sidhwa
# } Driver Code Ends