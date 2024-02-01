#User function Template for python3

import sys
from typing import List
sys.setrecursionlimit(10**8)
class Solution:
    def countDistinctIslands(self, grid : List[List[int]]) -> int:
        islands = set()

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    shape = []
                    self.dfs(grid, r, c, shape, 0)  # Pass direction as an argument
                    islands.add(tuple(shape))

        return len(islands)
        
        
        

    def dfs(self, grid, r, c, shape, direction):
        if 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] == 1:
            grid[r][c] = 0  # Mark visited cell
            shape.append(direction)  # Record direction

            self.dfs(grid, r - 1, c, shape, 1)  # Up
            self.dfs(grid, r + 1, c, shape, 2)  # Down
            self.dfs(grid, r, c - 1, shape, 3)  # Left
            self.dfs(grid, r, c + 1, shape, 4)  # Right

            shape.append(0) 

        # code here


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
        print(obj.countDistinctIslands(grid))
# } Driver Code Ends