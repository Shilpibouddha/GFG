#User function Template for python3

class Solution:

    def decodeIt(self, Str, k):
        new_str = ""
        size = len(Str)
    
        for i in range(size):
            if not Str[i].isdigit():
                new_str += Str[i]
            else:
                m = int(Str[i])
                res = new_str
                for j in range(1, m):
                    new_str += res
    
        return new_str[k - 1]
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        Str = input()
        k = int(input())

        solObj = Solution()

        print(solObj.decodeIt(Str, k))
# } Driver Code Ends