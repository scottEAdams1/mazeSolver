class Point:
    ##Creates a single point
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
class Line:
    ##Creates a single line between two points
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    ##Draws a line
    def draw(self, canvas, fill_colour):
        canvas.create_line(self.point1.x, self.point1.y,
        self.point2.x, self.point2.y, fill = fill_colour, width = 2)