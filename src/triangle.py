def area(a, h): 
    '''
    Вычисляет площадь треугольника.

    Аргументы:
        a (int): Длина основания треугольника.
        h (int): Высота, опущенная на основание.

    Возвращаемое значение:
        float: Площадь треугольника.

    Исключения:
        TypeError: Если аргументы не являются целыми числами.
        ValueError: Если аргументы меньше или равны 0.
    '''
    
    if (type(a) is not int or type (h) is not int):
        raise TypeError("Argument must be int")
        
    if (a <= 0 or h <= 0):
        raise ValueError("Arguments must be >0")
        
    return a * h / 2 

def perimeter(a, b, c): 
    '''
    Вычисляет периметр треугольника по трем сторонам.

    Аргументы:
        a (int): Первая сторона.
        b (int): Вторая сторона.
        c (int): Третья сторона.

    Возвращаемое значение:
        int: Периметр треугольника.

    Исключения:
        TypeError: Если стороны не являются целыми числами.
        ValueError: Если стороны меньше или равны 0.
    '''
    
    if (type(a) is not int or type (b) is not int or type (c) is not int):
        raise TypeError("Argument must be int")
        
    if (a <= 0 or b <= 0 or c <= 0):
        raise ValueError("Arguments must be >0")
    
    return a + b + c
