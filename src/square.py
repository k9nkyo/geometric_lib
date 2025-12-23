
def area(a):
    '''На вход подается сторона квадрата, возвращает площадь квадрата'''
    
    if (type(a) is not int):
        raise TypeError("Argument must be int")
        
    if (a <= 0):
        raise ValueError("Argument must be >0")
        
    return a * a


def perimeter(a):
    '''На вход подается сторона квадрата, возвращает периметр квадрата'''
    
    if (type(a) is not int):
        raise TypeError("Argument must be int")
        
    if (a <= 0):
        raise ValueError("Argument must be >0")
        
    return 4 * a
