# Math formulas
## Area
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²
- Triangle: S = ½ah

## Perimeter
- Circle: P = 2πR
- Rectangle: P = 2(a + b)
- Square: P = 4a
- Triangle: P = a + b + c

# Functions
## Circle
### Area evaluation
The function takes the radius of the circle `r` and returns its area.
```python
def area(r):
    '''
    Аргументы:
        r (int): радиус круга
    Возвращает:
        float: площадь круга
    '''
```

>Example: area(1) returns 3.14159265359

### Perimeter evaluation
The function takes the radius `r` and returns the circumference.
```python
def perimeter(r):
    '''
    Аргументы:
        r (int): радиус круга
    Возвращает:
        float: длина окружности
    '''
```

>Example: perimeter(1) returns 6.28318530718

##Rectangle
### Area evaluation
The function takes the lengths of two sides `a` and `b` and returns the area of the rectangle.
```python
def area(a, b):
    '''
    Аргументы:
        a (int): сторона a
        b (int): сторона b
    Возвращает:
        int: площадь прямоугольника
    '''
```

>Example: area(1,2) returns 2

### Perimeter evaluation
The function takes the lengths of sides `a` and `b` and returns the perimeter of the rectangle.
```python
def perimeter(a, b):
    '''
    Аргументы:
        a (int): сторона a
        b (int): сторона b
    Возвращает:
        int: периметр прямоугольника
    '''
```

>Example: perimeter(1, 2) returns 6

## Square
### Area evaluation
The function takes the length of the side of the square `a` and returns its area.
```python
def area(a):
    '''
    Аргументы:
        a (int): сторона квадрата
    Возвращает:
        int: площадь квадрата
    '''
```

>Example: area(2) returns 4

### Perimeter evaluation
The function takes the length of the side of the square `a` and returns its perimeter.
```python
def perimeter(a):
    '''
    Аргументы:
        a (int): сторона квадрата
    Возвращает:
        int: периметр квадрата
    '''
```

>Example: perimeter(1) returns 4

## Triangle
### Area evaluation
The function takes the base `a` and height `h` and returns the area of the triangle.
```python
def area(a, h):
    '''
    Аргументы:
        a (int): основание
        h (int): высота
    Возвращает:
        float: площадь треугольника
    '''
```

>Example: area(1, 2) returns 1

### Perimeter evaluation
The function takes three sides `a`, `b`, `c` and returns the perimeter of the triangle.
```python
def perimeter(a, b, c):
    '''
    Аргументы:
        a, b, c (int): стороны треугольника
    Возвращает:
        int: периметр треугольника
    '''
```

>Example: perimeter(1, 2, 3) returns 6

# Changelog
- [Added documentation](https://github.com/k9nkyo/geometric_lib/commit/8d906969dc5933e045f5a064d2afb9b089cb978a)
- [Added triangle](https://github.com/k9nkyo/geometric_lib/commit/c75468fd16ef8d6d42d5ab481f79fb0d42a5714a)
- [Added rectangle](https://github.com/k9nkyo/geometric_lib/commit/98ba15559eb969a9d25e2cc447cbe28d5f0962e8)
- [L-03: Docs added](https://github.com/k9nkyo/geometric_lib/commit/d078c8d9ee6155f3cb0e577d28d337b791de28e2)
- [L-03: Circle and square added](https://github.com/k9nkyo/geometric_lib/commit/8ba9aeb3cea847b63a91ac378a2a6db758682460)





