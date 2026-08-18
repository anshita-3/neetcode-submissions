class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        count=0
        res=[]
        def dfs(r,c):
            nonlocal area
            if r<0 or r>=rows or c<0 or c>=cols:
                return 
            if grid[r][c]==0:
                return 
            grid[r][c]=0
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
            area+=1
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1:
                    area=0
                    dfs(r,c)
                    res.append(area)
        return max(res,default=0)

            