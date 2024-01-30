#User function Template for python3

import sys
sys.setrecursionlimit(10**8)
class Solution:
    def numIslands(self,grid):
        n = len(grid)
        m = len(grid[0])
        q = []
        vis = [[0 for i in range(m)]for i in range(n)]
        count = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 and vis[i][j] == 0:
                    count += 1
                    q.append([i, j])
                    vis[i][j] = 1
                    while q:
                        r = q[0][0]
                        c = q[0][1]
                        q.pop(0)
                        for dr in range(-1, 2):
                            for dc in range(-1, 2):
                                nr = r + dr
                                nc = c + dc
                                if nr >= 0 and nr < n and nc >= 0 and nc < m and grid[nr][nc] == 1 and vis[nr][nc] == 0:
                                    q.append([nr, nc])
                                    vis[nr][nc] = 1
        return count
        #code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    for _ in range(int(input())):
        n,m=map(int,input().strip().split())
        grid=[]
        for i in range(n):
            grid.append([int(i) for i in input().strip().split()])
        obj=Solution()
        print(obj.numIslands(grid))
# } Driver Code Ends