from Surface import Surface 
from Rectangle import Rectangle

def main(): 
    """
    This function uses two assertion tests, one for reactangle and one for surface, by changing the dimensions of the rectangle and making sure all of the instance variables and imports work properly 
    args: None 
    returns: None, if the whole test ran correctly, "Test Complete!" prints to the command line 
    
    """
    ## Rectangle Assertion Test ##
    r = Rectangle(10, 10, 10, 10)
    assert((r.x, r.y, r.height, r.width) == (10,10,10,10))
    r = Rectangle(-1, 1, 1, 1)
    assert((r.x, r.y, r.height, r.width) == (1,1,1,1))
    r = Rectangle(1, -5, 1, 1)
    assert((r.x, r.y, r.height, r.width) == (1,5,1,1))
    r = Rectangle(1, 1, -10, 1)
    assert((r.x, r.y, r.height, r.width) == (1,1,10,1))
    r = Rectangle(1, 1, 1, -1000)
    assert((r.x, r.y, r.height, r.width) == (1,1,1,1000))
    ## Surface Assertion Test ##
    s = Surface("myimage.png", 10, 10, 10, 10)
    assert((s.rect.x, s.rect.y, s.rect.height, s.rect.width) == (10,10,10,10))
    srect = s.getRect()
    assert((srect.x,  s.getRect().y, srect.height,  srect.width) == (10,10,10,10))
    assert s.image
    print("Test Complete!")

main()
