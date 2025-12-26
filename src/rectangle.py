def area(a, b): 
    '''
    Вычисляет площадь прямоугольника по двум сторонам.

    Аргументы:
        a (int): Длина первой стороны.
        b (int): Длина второй стороны.

    Возвращаемое значение:
        int: Площадь прямоугольника.

    Исключения:
        TypeError: Если одна из сторон не является целым числом.
        ValueError: Если одна из сторон меньше или равна 0.
    '''
    
    if (type(a) is not int or type(b) is not int):
        raise TypeError("Argument must be int")
        
    if (a <= 0 or b <= 0):
        raise ValueError("Argument must be >0")
    
    return a * b 

def perimeter(a, b): 
    '''
    Вычисляет периметр прямоугольника.

    Аргументы:
        a (int): Длина первой стороны.
        b (int): Длина второй стороны.

    Возвращаемое значение:
        int: Периметр прямоугольника.

    Исключения:
        TypeError: Если одна из сторон не является целым числом.
        ValueError: Если одна из сторон меньше или равна 0.
    '''
    
    if (type(a) is not int or type(b) is not int):
        raise TypeError("Argument must be int")
    
    if (a <= 0 or b <= 0):
        raise ValueError("Argument must be >0")
    
    return 2*(a + b)
