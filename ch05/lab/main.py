import pygame as pg 


def threenp1(n):
    count = 0 
    while n > 1:
       if n % 2 == 0:
        n = int(n / 2)
        count += 1
       else:
        n = int(3 * n + 1)
        count += 1
    return count

threenplus1_iters_dict = set()

def counter(): 
    #upper_limit = int(input("Define an Upper Limit: "))
    for num in range(2, upper_limit):
        iters = threenp1(num)
        print("Number of Iterations: ", counter)
        threenplus1_iters_dict.add((num, iters))
    return(num, iters) 

def graph_coordinates(threenplus1_iters_dict): 
   display = pg.display.set_mode() 
   points = list(threenplus1_iters_dict.items()) 
   print(points)
   pg.display.flip()
   pg.draw.lines(points)
   new_display = pg.transform.flip(display, False, True)
   width, height = new_display.get_size()
   display.blit(new_display, (0,0))
   new_display = pg.transform.scale(new_display, (width * 5, height * 5)) 
   for iters in threenplus1_iters_dict: 
        max_so_far = str( max(iters))

   font = pg.font.Font(None, 14)
   msg = font.render("This is the Max So Far: ",max_so_far, True, 'red') 
   display.blit(msg, (10,10))
   return None 


def main(): 
   pg.init() 
   upper_limit = int(input("Define an Upper Limit: "))
   counter(upper_limit)
   graph_coordinates(threenplus1_iters_dict)

