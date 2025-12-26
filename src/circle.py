import math


def area(r):
    '''
    Вычисляет площадь круга по заданному радиусу.

    Аргументы:
        r (int): Радиус круга. 

    Возвращаемое значение:
        float: Площадь круга.

    Исключения:
        TypeError: Если радиус не является целым числом.
        ValueError: Если радиус меньше или равен 0.
    '''

    if (type(r) is not int):
        raise TypeError("Argument must be int")
    
    if (r<= 0):
        raise ValueError("Argument must be >0")
        
    return math.pi * r * r



def perimeter(r):
    '''
    Вычисляет длину окружности (периметр) по заданному радиусу.

    Аргументы:
        r (int): Радиус окружности.

    Возвращаемое значение:
        float: Длина окружности.

    Исключения:
        TypeError: Если радиус не является целым числом.
        ValueError: Если радиус меньше или равен 0.
    '''
    
    if (type(r) is not int):
        raise TypeError("Argument must be int")
        
    if (r<=0):
        raise ValueError("Argument must be >0")
        
    return 2 * math.pi * r

