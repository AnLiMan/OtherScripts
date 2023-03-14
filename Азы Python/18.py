#Первая часть
print ('\nПервая часть')

def PrintFunc(size, text):
    print('Размер: ', size,';', 'Текст: ', text)
print ('\nБез позиционных аргументов')
PrintFunc(48, 'Мдя...')
print ('\nc позиционными аргументами')
PrintFunc(text = 'Мдя...',size = 48)

#Вторая часть
print ('\nВторая часть')

def PrintFunc2(size = 0, text = 'Text'):
    print('Размер: ', size,';', 'Текст: ', text)
print ('\nБез одного аргумента')
PrintFunc2(size = 48)
print ('\nБез двух аргументов>')
PrintFunc2()

#Третья часть
print ('\nТретья часть')

def PrintFunc3(city = 'No City', Country = 'No Country'):
    print('Город ', city,'в', 'Стране - ', Country)

print ('\nПросто список')
PrintFunc3('Челябинск','Рашка')
PrintFunc3('Нью-Йорк','США')
PrintFunc3('Барселона','Испания')
print ('\nБез двух аргументов>')
PrintFunc3()