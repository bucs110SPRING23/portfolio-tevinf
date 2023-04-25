from Rectangle import Rectangle

class Surface: 
    def __init__(self, filename, x, y, h, w):
        self.image = str(filename) 
        self.rect = Rectangle(x, y, h, w)
    def getRect(self):
        """
        This function returns the self.rect object whihc is a rectangle with the attributes x, y, width (w), and height(h)
        args: (self) the function calls itself to get data from the init function before it 
        return: (Rectangle object) this returns the rectangle object from line 6 
        """
        return self.rect 
    