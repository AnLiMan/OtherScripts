print("\nПервая часть")
print('Введите марку машины')
car = input()
print('Вы быбрали: ', car)

print("\nВторая часть")
print('Введите кол-во мест')
number = int (input())
if (number <  8 or number == 8):
    print('Столик забронирован')
else:
    print('Придется подождать')

print("\nТретья часть")
print('Введите число')
number2 = int (input())
if (number2 % 10 == 0):
    print('Число кратно 10')
else:
    print('Число не кратно 10')