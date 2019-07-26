import turtle

def polygon(sides:int, length:int):
    """The function draws polygon of various sizes
    
    Arguments:
        sides {int} -- The number of sides of the polygon
        length {int} -- The length of each side of the polygon in pixels
    """
    # (sides - 2) * 180 -- defines sum of angles in any polygon
    angle = ((sides - 2) * 180) / sides

    for x in range(sides):
        turtle.forward(length)
        turtle.left(180 - angle)
        

def rectangle(length:int, breadth:int):
    """The function draws rectangle
    
    Arguments:
        length {int} -- The length of the quadrilateral in pixels
        breadth {int} -- The breadth of the quadrilateral in pixels
    """
    
    for x in range(2):
        turtle.forward(length)
        turtle.right(90)
        turtle.forward(breadth)
        turtle.right(90)