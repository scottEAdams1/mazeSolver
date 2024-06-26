from window import Window
from line import Line, Point
from cell import Cell

def main():
    win = Window(800, 600)
    point1 = Point(0, 0)
    point2 = Point(599, 599)
    line = Line(point1, point2)
    #win.draw_line(line, "red")
    cell = Cell(win)
    cell.draw(0, 0, 50, 50)
    win.wait_for_close()

main()