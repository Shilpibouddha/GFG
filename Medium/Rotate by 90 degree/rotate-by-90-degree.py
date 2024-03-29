#User function Template for python3

def rotate(matrix): 
    for i in range(len(matrix)):
        for j in range(0,i):
        # swaping the number to find transpose
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    matrix.reverse() # reverse the transpose
 
    return matrix

#{ 
 # Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__':
	t = int(input())
	for _ in range(t):
		N=int(input())
		arr=[int(x) for x in input().split()]
		matrix=[]

		for i in range(0,N*N,N):
			matrix.append(arr[i:i+N])

		rotate(matrix)
		for i in range(N): 
			for j in range(N): 
				print(matrix[i][j], end =' ') 
			print() 
        

# } Driver Code Ends