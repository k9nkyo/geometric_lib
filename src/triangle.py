def area(a, h): 
    '''На вход подаются основание и высота треугольника, возвращает площадь треугольника'''
    
    if (type(a) is not int or type (h) is not int):
        raise TypeError("Argument must be int")
        
    if (a <= 0 or h <= 0):
        raise ValueError("Arguments must be >0")
        
    return a * h / 2 

def perimeter(a, b, c): 
    '''на вход подаются три стороны треугольника, возвращает периметр треугольника'''
    
    if (type(a) is not int or type (b) is not int or type (c) is not int):
        raise TypeError("Argument must be int")
        
    if (a <= 0 or b <= 0 or c <= 0):
        raise ValueError("Arguments must be >0")
    
    return a + b + c
