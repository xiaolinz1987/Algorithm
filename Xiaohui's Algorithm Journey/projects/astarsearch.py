class Grid:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.F = 0
        self.G = 0
        self.H = 0
        self.parent = None

    def init_grid(self, parent, end):
        self.parent = parent
        if parent is not None:
            self.G = parent.G + 1
        else:
            self.G = 1
        self.H = abs(self.x - end.x) + abs(self.y - end.y)
        self.F = self.G + self.H

class MyAStarSearch:

    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __find_min_grid(self, open_list=[]):
        temp_grid = open_list[0]
        for grid in open_list:
            if grid.F < temp_grid.F:
                temp_grid = grid
        return temp_grid

    def contain_grid(self, grids, x, y):
        for grid in grids:
            if grid.x == x and grid.y == y:
                return True
        return False

    def __is_valid_grid(self, x, y, open_list=[], close_list=[]):
        if x < 0 or x >= len(MAZE) or y < 0 or y >= len(MAZE[0]):
            return False    
        if MAZE[x][y] == 1:
            return False
        if self.contain_grid(open_list, x, y):
            return False
        if self.contain_grid(close_list, x, y):
            return False
        return True
    
    def __find_neighbors(self, grid, open_list=[], close_list=[]):
        grid_list = []
        if self.__is_valid_grid(grid.x, grid.y-1, open_list, close_list):
            grid_list.append(Grid(grid.x, grid.y-1))
        if self.__is_valid_grid(grid.x, grid.y+1, open_list, close_list):
            grid_list.append(Grid(grid.x, grid.y+1))
        if self.__is_valid_grid(grid.x-1, grid.y, open_list, close_list):
            grid_list.append(Grid(grid.x-1, grid.y))
        if self.__is_valid_grid(grid.x+1, grid.y, open_list, close_list):
            grid_list.append(Grid(grid.x+1, grid.y))
        return grid_list

    def a_star_search(self):
        open_list = []
        close_list = []
        open_list.append(self.start)

        while len(open_list) > 0:
            current_grid = self.__find_min_grid(open_list)
            open_list.remove(current_grid)
            close_list.append(current_grid)

            neighbors = self.__find_neighbors(current_grid, open_list, close_list)
            for grid in neighbors:
                if grid not in open_list:
                    grid.init_grid(current_grid, self.end)
                    open_list.append(grid)
            
            for grid in open_list:
                if grid.x == self.end.x and grid.y == self.end.y:
                    return grid

        return None
    
MAZE = [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0]
        ]

start = Grid(2, 1)
end = Grid(2, 5)
astar = MyAStarSearch(start, end)
result = astar.a_star_search()

path = []
while result is not None:
    path.append(Grid(result.x, result.y))
    result = result.parent

for i in range(0, len(MAZE)):
    for j in range(0, len(MAZE[0])):
        if astar.contain_grid(path, i, j):
            print("*, ", end = '')
        else:
            print(str(MAZE[i][j]) + ", ", end = '')

