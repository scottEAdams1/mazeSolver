from tkinter import Tk, BOTH, Canvas
from line import Line

class Window:
    ##Constructor
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title = "Maze Solver"
        self.__canvas = Canvas(self.__root, bg = "light blue", height = height, width = width)
        self.__canvas.pack(fill = BOTH, expand = 1)
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    ##Redraw the graphics
    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    ##Call redraw continuously
    def wait_for_close(self):
        self.__running = True
        while self.__running == True:
            self.redraw()
        
    ##Close the window
    def close(self):
        self.__running = False

    ##Draws a line in the window
    def draw_line(self, line, fill_colour):
        line.draw(self.__canvas, fill_colour)

