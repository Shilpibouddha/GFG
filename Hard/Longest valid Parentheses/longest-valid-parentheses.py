# User function Template for Python3

class Solution:
    def maxLength(self, S):
        left = 0
        right = 0
        max_length = 0

    # Forward pass
        for i in range(len(S)):
            if S[i] == '(':
                left += 1
            else:
                right += 1

            if left == right:
                max_length = max(max_length, left * 2)
            elif right > left:
                left = 0
                right = 0

    # Backward pass
        left = 0
        right = 0

        for i in range(len(S) - 1, -1, -1):
            if S[i] == '(':
                left += 1
            else:
                right += 1

            if left == right:
                max_length = max(max_length, left * 2)
            elif left > right:
                left = 0
                right = 0

        return max_length
       
#{ 
 # Driver Code Starts
# Initial Template for Python3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        S = input()
        
        ob = Solution()
        print(ob.maxLength(S))
# } Driver Code Ends