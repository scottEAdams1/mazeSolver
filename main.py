from window import Window
from line import Line, Point
from cell import Cell

def main():
    win = Window(800, 600)
    point1 = Point(0, 0)
    point2 = Point(599, 599)
    line = Line(point1, point2)
    #win.draw_line(line, "red")
    cell1 = Cell(win)
    cell2 = Cell(win)
    cell1.draw(1, 1, 50, 50)
    cell2.draw(51, 1, 101, 50)
    cell1.draw_move(cell2, True)
    win.wait_for_close()

main()