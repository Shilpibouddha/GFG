#User function template for Python 3

class Solution:
    def majorityElement(self, A, N):
        dct={}
        for i in A:
            if i in dct:
                dct[i]+=1
            else:
                dct[i]=1
            if dct[i]>N//2:
                return i
        return -1
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

from sys import stdin


def main():
        T=int(input())
        while(T>0):
            
            N=int(input())

            A=[int(x) for x in input().strip().split()]
            
            
            obj = Solution()
            print(obj.majorityElement(A,N))
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends