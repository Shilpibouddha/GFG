#User function Template for python3

class Solution:

    def reverseAlternate(self, Str):
        words = Str.split(' ')
        for i in range(1, len(words), 2):
            words[i] = words[i][::-1]
        reversed_string = ' '.join(words)
        return reversed_string
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):

        Str = input()

        solObj = Solution()

        print(solObj.reverseAlternate(Str))

# } Driver Code Ends