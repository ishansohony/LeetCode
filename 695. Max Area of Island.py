class Solution:
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        def dfs(grid, row, col, count):
            if(row >= len(grid) or row < 0 or col >= len(grid[0]) or col < 0):
                return count
            
            if(grid[row][col] == 1):
                count += 1
                grid[row][col] = 0
                count = dfs(grid, row + 1, col, count)
                count = dfs(grid, row - 1, col, count)
                count = dfs(grid, row, col + 1, count)
                count = dfs(grid, row, col - 1, count)
                
            return count
                   
        
        
        max_area = 0
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    count = 0
                    area = dfs(grid, row, col, count)
                    print(area)
                    if(area > max_area):
                        max_area = area
                        
        return max_area
                        
        
