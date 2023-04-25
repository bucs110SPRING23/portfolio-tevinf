class Rectangle:
    def __init__ (self, x, y, h, w): 
        self.x = abs(x)
        self.y = abs(y)
        self.height = abs(h)
        self.width = abs(w)
        return None
    def __str__(self): 
        """ 
        This funtion takes the instance variables from init and formats them as a string 
        args: (Self) the function calls itself to return the characteristics of the rectangle object 
        return: (str) the function returns the x, y, width, and height of the rectangle object as a string 
        """
        myoutput = ("(x: {self.x}, y: {self.y}), width: {self.width}, height: {self.height}")
        return myoutput 