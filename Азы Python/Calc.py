# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 17:25:32 2019

@author: Student
"""

print ('Калькуляр')
print('Что делаем? +, -, /, *')

InputData = input()

if InputData == '+':
    print("Введите x ")
    x = float (input())
    print("Введите y ")
    y = float (input())
    sum = x+y
    print(sum)
    
elif InputData == '-':
    print("Введите x ")
    x1 = float (input())
    print("Введите y ")
    y2 = float (input())
    rasn = x-y
    print(rasn)
            
elif InputData == '*':
    print("Введите x ")
    x3 = float (input())
    print("Введите y ")
    y3 = float (input())
    umn = x*y
    print(umn)
            
elif InputData == '/':
    print("Введите x ")
    x4 = float (input())
    print("Введите y ")
    y4 = float (input())
    delen = x/y
    print(delen)


try: # Пробуем что-то сделать
     k = 1 / 0 # Деление на ноль
except ZeroDivisionError: # Отслеживаем на арифметическую ошибку
     print ("Найдена ошибка") # Мы нашли ошибку
     k = 0 # Наша переменная теперь будет равна 0

print(k) # Просто выводим переменную


            
    




