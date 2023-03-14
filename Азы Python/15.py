print("\nПервая часть")
PizzaList = []
inputData = True
print('Введите название пиццы, когда закончите введите "quit"')
while inputData == True:
    Data = str (input())
    PizzaList.append(Data)
    if (Data == 'quit'):
        inputData = False
        PizzaList.remove(Data)
print(PizzaList)

print("\nВторая часть")
print('Введите ваш возраст: ')
number = int (input())
if number < 3 or number == 3:
    print('Билет бесплатный')
if (number < 12 and number > 3):
    print('Билет стоит 10$')
if (number > 12 or number == 12):
    print('Билет стоит 10$')

print("\nТретья часть")
while 1 < 2:
    print('Это будет продолжаться вечно...')
