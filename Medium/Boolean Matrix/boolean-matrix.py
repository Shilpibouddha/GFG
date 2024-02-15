#User function Template for python3


#Function to modify the matrix such that if a matrix cell matrix[i][j]
#is 1 then all the cells in its ith row and jth column will become 1.
def booleanMatrix(matrix):

    r = len(matrix)  
    c = len(matrix[0]) 

    R = [0] * r
    C = [0] * c

    for i in range(r):
        for j in range(c):
            if matrix[i][j] == 1:
                R[i] = 1
                C[j] = 1
    
    for i in range(r):
        for j in range(c):
            matrix[i][j] = R[i] or C[j]


    # code here 


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        r,c = map(int, input().strip().split())
        matrix = []
        for i in range(r):
            line = [int(x) for x in input().strip().split()]
            matrix.append(line)
        booleanMatrix(matrix)
        for i in range(r):
            for j in range(c):
                print(matrix[i][j], end=' ')
            print()


# } Driver Code Ends