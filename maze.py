from cell import Cell
import time, random

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols,
    cell_size_x, cell_size_y, win = None, seed = None):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        if seed:
            random.seed(seed)
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)

    ##Creates cells for the entire maze
    def _create_cells(self):
        self._cells = []
        for i in range(self._num_cols):
            cell_col = []
            for j in range(self._num_rows):
                cell_col.append(Cell(self._win))
            self._cells.append(cell_col)
        for i in range(len(self._cells)):
            for j in range(len(self._cells[i])):
                self._draw_cell(i, j)

    ##Draws an individual cell at the right location
    def _draw_cell(self, i, j):
        x = self._x1 + i * self._cell_size_x
        y = self._y1 + j * self._cell_size_y
        self._cells[i][j].draw(x, y, x + self._cell_size_x, y + self._cell_size_y)
        self._animate()

    ##Redraws the window every 0.05 seconds to update the cells
    def _animate(self):
        if self._win != None:
            self._win.redraw()
            time.sleep(0.05)

    ##Adds an entrance and exit to the maze
    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        self._cells[self._num_cols - 1][self._num_rows - 1].has_bottom_wall = False
        self._draw_cell(self._num_cols - 1, self._num_rows - 1)

    ##Breaks walls to make paths through the maze
    def _break_walls_r(self, i, j):
        self._cells[i][j]._visited = True
        while True:
            possible = []
            if i > 0 and self._cells[i - 1][j]._visited == False:
                possible.append([i - 1, j])
            if i < self._num_cols - 1 and self._cells[i + 1][j]._visited == False:
                possible.append([i + 1, j])
            if j > 0 and self._cells[i][j - 1]._visited == False:
                possible.append([i, j - 1])
            if j < self._num_rows - 1 and self._cells[i][j + 1]._visited == False:
                possible.append([i, j + 1])
            if len(possible) == 0:
                self._draw_cell(i, j)
                return
            else:
                direction = possible[random.randrange(len(possible))]
                if direction[0] == i + 1:
                    self._cells[i][j].has_right_wall = False
                    self._cells[i + 1][j].has_left_wall = False
                if direction[1] == j + 1:
                    self._cells[i][j].has_bottom_wall = False
                    self._cells[i][j + 1].has_top_wall = False
                if direction[0] == i - 1:
                    self._cells[i][j].has_left_wall = False
                    self._cells[i - 1][j].has_right_wall = False
                if direction[1] == j - 1:
                    self._cells[i][j].has_top_wall = False
                    self._cells[i][j - 1].has_bottom_wall = False
                self._break_walls_r(direction[0], direction[1])
            


