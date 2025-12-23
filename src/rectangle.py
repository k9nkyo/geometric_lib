def area(a, b): 
    '''На вход подаются две стороны прямоугольника, возвращает площадь прямоугольника'''
    
    if (type(a) is not int or type(b) is not int):
        raise TypeError("Argument must be int")
        
    if (a <= 0 or b <= 0):
        raise ValueError("Argument must be >0")
    
    return a * b 

def perimeter(a, b): 
    '''На вход подаются двае стороны прямоугольника, возвращает периметр прямоугольника'''
    
    if (type(a) is not int or type(b) is not int):
        raise TypeError("Argument must be int")
    
    if (a <= 0 or b <= 0):
        raise ValueError("Argument must be >0")
    
    return 2*(a + b)
