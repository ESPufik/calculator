import math
import fractions
import cmath

class AdvancedCalculator:
    def __init__(self):
        pass

    def add(self, *args):
        return sum(args)

    def subtract(self, x, y):
        return x - y

    def multiply(self, *args):
        result = 1
        for num in args:
            result *= num
        return result

    def divide(self, x, y):
        if y == 0:
            return "Ошибка: деление на ноль"
        else:
            return x / y

    def power(self, x, y):
        return x ** y

    def factorial(self, x):
        if x == 0:
            return 1
        else:
            return x * self.factorial(x - 1)

    def square_root(self, x):
        if x < 0:
            return "Ошибка: квадратный корень из отрицательного числа"
        else:
            return math.sqrt(x)

    def cube_root(self, x):
        return x ** (1/3)

    def nth_root(self, x, n):
        if x < 0 and n % 2 == 0:
            return "Ошибка: извлечение корня n-ой степени из отрицательного числа с четным n"
        else:
            return x ** (1/n)

    def fraction(self, x, y):
        return fractions.Fraction(x, y)

    def complex_add(self, x1, y1, x2, y2):
        return complex(x1, y1) + complex(x2, y2)

    def complex_subtract(self, x1, y1, x2, y2):
        return complex(x1, y1) - complex(x2, y2)

    def complex_multiply(self, x1, y1, x2, y2):
        return complex(x1, y1) * complex(x2, y2)

    def complex_divide(self, x1, y1, x2, y2):
        return complex(x1, y1) / complex(x2, y2)

calc = AdvancedCalculator()

print("Выберите операцию:")
print("1. Сложение")
print("2. Вычитание")
print("3. Умножение")
print("4. Деление")
print("5. Возведение в степень")
print("6. Факториал")
print("7. Квадратный корень")
print("8. Кубический корень")
print("9. Извлечение корня n-ой степени")
print("10. Создать обыкновенную дробь")
print("11. Сложение комплексных чисел")
print("12. Вычитание комплексных чисел")
print("13. Умножение комплексных чисел")
print("14. Деление комплексных чисел")

choice = input("Введите номер операции (1-14): ")

if choice in ['1', '3']:
    nums = input("Введите числа через пробел: ").split()
    nums = [float(num) for num in nums]
    if choice == '1':
        print("Результат:", calc.add(*nums))
    elif choice == '3':
        print("Результат:", calc.multiply(*nums))
else:
    num1 = float(input("Введите первое число: "))
    if choice not in ['6', '7', '8', '9']:
        num2 = float(input("Введите второе число: "))

    if choice == '1':
        print("Результат:", calc.add(num1, num2))
    elif choice == '2':
        print("Результат:", calc.subtract(num1, num2))
    elif choice == '3':
        print("Результат:", calc.multiply(num1, num2))
    elif choice == '4':
        print("Результат:", calc.divide(num1, num2))
    elif choice == '5':
        print("Результат:", calc.power(num1, num2))
    elif choice == '6':
        print("Результат:", calc.factorial(num1))
    elif choice == '7':
        print("Результат:", calc.square_root(num1))
    elif choice == '8':
        print("Результат:", calc.cube_root(num1))
    elif choice == '9':
        root = float(input("Введите степень корня: "))
        print("Результат:", calc.nth_root(num1, root))
    elif choice == '10':
        num2 = float(input("Введите второе число (знаменатель): "))
        print("Результат:", calc.fraction(num1, num2))
    elif choice in ['11', '12', '13', '14']:
        num2 = float(input("Введите второе число (мнимую часть для комплексного числа): "))
        num3 = float(input("Введите третье число (действительную часть для второго комплексного числа): "))
        num4 = float(input("Введите четвёртое число (мнимую часть для второго комплексного числа): "))
        if choice == '11':
            print("Результат:", calc.complex_add(num1, num2, num3, num4))
        elif choice == '12':
            print("Результат:", calc.complex_subtract(num1, num2, num3, num4))
        elif choice == '13':
            print("Результат:", calc.complex_multiply(num1, num2, num3, num4))
        elif choice == '14':
            print("Результат:", calc.complex_divide(num1, num2, num3, num4))
    else:
        print("Ошибка: Неправильный ввод")
