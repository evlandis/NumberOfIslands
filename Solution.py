class Solution(object):
    def numIslands(self, grid):
        #for empty grids
        if not grid:
            return 0
        
        rows, columns = len(grid), len(grid[0])
        visit = set()
        islands=0
        
        #bfs is a iterative algorithm
        def bfs(r,c):
            q = collections.deque()
            visit.add((r,c))
            q.append((r,c))
            
            #this while loop checks nearby land to expand the land of an island
            while q:
                row, col = q.popleft()
                #checks each element right,left,up, and down
                directions = [[1,0],[-1,0],[0,1],[0,-1]]
                for dr, dc in directions:
                    r, c=row+dr, col+dc
                    #if statement checks for the position being "in bounds"
                    #checks if this position is land
                    #checks to make sure the position is not already visited
                    if (r in range(rows) and 
                        c in range(columns) and
                        grid[r][c]=="1" and 
                        (r,c) not in visit):
                        q.append((r, c))
                        visit.add((r,c))
        
        #iterates through rows and columns
        #uses bfs from previous function
        for r in range(rows):
            for c in range(columns):
                #if an island and not visited yet
                if grid[r][c]=="1" and (r,c) not in visit:
                    bfs(r,c)
                    islands+=1
        return islands
