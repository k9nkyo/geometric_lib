import math


def area(r):
    '''Принимает число r, возвращает площадь фигуры'''

    if (type(r) is not int):
        raise TypeError("Argument must be int")
    
    if (r<= 0):
        raise ValueError("Argument must be >0")
        
    return math.pi * r * r



def perimeter(r):
    '''Принимает число r, возвращает периметр фигуры'''
    
    if (type(r) is not int):
        raise TypeError("Argument must be int")
        
    if (r<=0):
        raise ValueError("Argument must be >0")
        
    return 2 * math.pi * r

