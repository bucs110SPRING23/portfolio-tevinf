# class == type 
# classes are user-defined types (type not in python) 
# 'complex-type' is a class made up of different types 
# classes data is referred to as instance variables 


#import turtle 
class Num: 

    def __init__(self, n): 
        self.data = n #this is now the instance variables for Num type objects 
        self.x = "string" 

        #object functions are called methods
        #using self as the first parameter makes it a method
    def addone(self): 
        self.data += 1

#class Foo: 
    #def __init__(self, **kwargs): #**kwargs is using a list as a parameter 
        #self.__dict__ = kwargs 
        #print(kwargs)
    


def main(): 

    mynum = Num(7) 
    #mynum2 = Num(9) 
    #mynum3 = {'data':7, "x" : "string"}

    print(mynum.data)
    #print(mynum2.data) 
    #print(mynum3["data"])
    #print(mynum.__dict__) 

    mynum.addone()
    print(mynum.data)

    #dictionary = {'x': 1, 'y': 2, 'z': 3}
    #foo = Foo(**dictionary) # as if it were x = 1, y = 2, z = 3

    #t = turtle.Turtle()
    #t.forward(56) 

    #mylist = [] # this means list(), str() is mylist = "" 
    #mylist.forward() # Error 
    #mylist.append()
    #index = 0 
    #mylist.pop(index) 



main()
