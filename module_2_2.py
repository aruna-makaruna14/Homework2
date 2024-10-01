first = int(input('Введите чило от 1 до 100: '))
print(first)
second = int(input('Введите чило от 1 до 100: '))
print(second)
third = int(input('Введите чило от 1 до 100: '))
print(third)
if first == second == third:
        print(3)
elif first == second != third or first == third != second or second == third != first:
        print(2)
elif first != second != third:
        print(0)