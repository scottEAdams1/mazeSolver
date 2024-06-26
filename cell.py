from window import Window
from line import Point, Line

class Cell:
    def __init__(self, window=None):
        ##Which wall exist
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        ##Coordinates of top left and bottom right
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self.__win = window

    ##Draw a single cell
    def draw(self, x1, y1, x2, y2):
        ##Coordinates of top left and bottom right
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        ##Draws individual walls of cells
        if self.__win != None:
            line = Line(Point(self._x1, self._y1), Point(self._x1, self._y2))
            if self.has_left_wall == True:
                self.__win.draw_line(line, "black")
            else:
                self.__win.draw_line(line, "light blue")
            line = Line(Point(self._x2, self._y1), Point(self._x2, self._y2))
            if self.has_right_wall == True:
                self.__win.draw_line(line, "black")
            else:
                self.__win.draw_line(line, "light blue")
            line = Line(Point(self._x1, self._y1), Point(self._x2, self._y1))
            if self.has_top_wall == True:
                self.__win.draw_line(line, "black")
            else:
                self.__win.draw_line(line, "light blue")
            line = Line(Point(self._x1, self._y2), Point(self._x2, self._y2))
            if self.has_bottom_wall == True:
                self.__win.draw_line(line, "black")
            else:
                self.__win.draw_line(line, "light blue")

    ##Draw a line between the centre of two cells
    def draw_move(self, to_cell, undo = False):
        centre1 = Point((self._x1 + self._x2) / 2,(self._y1 + self._y2) / 2)
        centre2 = Point((to_cell._x1 + to_cell._x2) / 2,(to_cell._y1 + to_cell._y2) / 2)
        line = Line(centre1, centre2)
        if undo == False:
            self.__win.draw_line(line, "red")
        else:
            self.__win.draw_line(line, "gray")
