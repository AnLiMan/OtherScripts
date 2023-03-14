#Первая часть
print('\nВведите green , red или yellow')
AlienColor = input()
if (AlienColor == 'green'):
    print('Вы заработали 5 очков')
else:
    print('')
print('Конец первой части')

#Вторая часть
print('\nВведите green , red или yellow')
AlienColor = input()
if (AlienColor == 'green'):
    print('Вы заработали 5 очков')
elif ((AlienColor == 'red')):
    print('Вы заработали 10 очков')
else:
    print('')
print('Конец второй части')

#Третья часть
print('\nВведите green , red или yellow')
AlienColor = input()
if (AlienColor == 'green'):
    print('Вы заработали 5 очков')
elif ((AlienColor == 'red')):
    print('Вы заработали 10 очков')
elif ((AlienColor == 'yellow')):
    print('Вы заработали 10 очков')
print('Конец третьей части')

#Четвертая часть
print('\nВведите свой возраст')
age = int (input())
if (age < 2):
    print('Младенец')
elif (age < 4 and age >= 2):
    print('Малыш')
elif (age < 13 and age >= 4):
    print('Ребёнок')
elif (age < 20 and age >= 13):
    print('Подросток')
elif (age < 65 and age >= 20):
    print('Взрослый')
elif (age >= 65):
    print('Пожилой')

print('Конец четвёртой части')

#Пятая часть
FavoriteFruits = ['фейхуа', 'киви', 'мандарины']
print('\nВведите название своего фрукта')
InputData = str (input())
if (InputData == FavoriteFruits[0]):
    print('Да, прикольно же звучит =) ?')
elif (InputData == FavoriteFruits[1]):
    print('Как птичка')
elif (InputData == FavoriteFruits[2]):
    print('Ноооовый год к нам мчится...')
else:
    print('Не угадали')