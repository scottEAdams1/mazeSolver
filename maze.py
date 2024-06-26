from cell import Cell
import time

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._create_cells()

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
        self._win.redraw()
        time.sleep(0.05)