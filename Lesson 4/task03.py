class Easy:
    """
    Это класс, вонструктор которого передается одно число
    Есть метод show, который распечатывает передаваемое число
    """

    def __init__(self, value):
        self.data = value

    def show(self):
        print(self.data)


class Diff(Easy):
    """
    Это класс, который наследует класс Easy, и принимает два числа
    Есть метод calc, который складывает передаваемые числа
    """

    def __init__(self, value, term):
        self.addendum = term
        super().__init__(value)

    def calc(self):
        return self.data + self.addendum


# s1 = Diff(1,5)
# s1.calc()

try:
    1 / 0
except ZeroDivisionError:
    print('division by zero. На 0 делить нельзя')
finally:
    print('Окончание теста')


def trace(fun):
    """
    Декоратор для распечатывания всех аргументов вызываемой функции
    """

    def inner(*args, **kwargs):
        print(fun.__name__, args, kwargs)
        return fun(*args, **kwargs)

    return inner


class HomeWork:
    """
    Класс, в котором применяется декоратор @property для доступа
    к внутренней переменной _v1
    """

    def __init__(self, *args):
        self._v1 = 42

    @property
    def data(self):
        return self._v1


def gen_to_ten():
    """
    Генератор от 1 до 10
    """
    t = 1
    i = 10
    while t < i:
        yield t
        t += 1


import collections

Point = collections.namedtuple('Point', ['x', 'y', 'z'])

# p = Point(37.401437, 1649, -116.86773)
