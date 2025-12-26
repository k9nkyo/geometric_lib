
def area(a):
    '''
    Вычисляет площадь квадрата.

    Аргументы:
        a (int): Сторона квадрата.

    Возвращаемое значение:
        int: Площадь квадрата.

    Исключения:
        TypeError: Если сторона не является целым числом.
        ValueError: Если сторона меньше или равна 0.
    '''
    
    if (type(a) is not int):
        raise TypeError("Argument must be int")
        
    if (a <= 0):
        raise ValueError("Argument must be >0")
        
    return a * a


def perimeter(a):
    '''
    Вычисляет периметр квадрата.
    
    Аргументы:
        a (int): Сторона квадрата.

    Возвращаемое значение:
        int: Периметр квадрата.

    Исключения:
        TypeError: Если сторона не является целым числом.
        ValueError: Если сторона меньше или равна 0.
    '''
    
    if (type(a) is not int):
        raise TypeError("Argument must be int")
        
    if (a <= 0):
        raise ValueError("Argument must be >0")
        
    return 4 * a
