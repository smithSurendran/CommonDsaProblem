class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols= len(grid), len(grid[0])
        minutes=0

        while True:
            changed=False
            new_grid= copy.deepcopy(grid)
            
            for i in range(rows):
                for j in range(cols):
                    if grid[i][j]==2:
                        for dy, dx in [(-1,0),(1,0),(0,-1),(0,1)]:
                            if   0<=i+dx<rows and 0<=j+dy<cols and grid[i+dx][j+dy]==1:
                                new_grid[i+dx][j+dy]=2
                                changed=True
            
            if not changed:
                break
            minutes+=1
            grid= new_grid

        for row in grid:
            if 1 in row:
                return -1
        return minutes