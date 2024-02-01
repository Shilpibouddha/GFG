#User function Template for python3

import sys
sys.setrecursionlimit(10**8)
class Solution:
    def numIslands(self,grid):
        islands = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    self.dfs(grid, r, c)
                    islands += 1

        return islands

    def dfs(self, grid, r, c):
        if 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] == 1:
            grid[r][c] = 0  # Mark visited cell

            directions = [(r-1, c-1), (r-1, c), (r-1, c+1),
                          (r, c-1), (r, c+1),
                          (r+1, c-1), (r+1, c), (r+1, c+1)]

            for row, col in directions:
                self.dfs(grid, row, col)


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