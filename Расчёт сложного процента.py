# -*- coding: utf-8 -*-
start = 100000 #Стартовая сумма
replenishment_amount = 100000 # Величина ежегодного пополнения
persent = 4 # Процент по банковскому депозиту
term_of_deposit = 42 # Срок вклада 
age = 23 # Текущий возраст
time_of_luxury = 15 # Время шикования (жизни)

for i in range (1, (term_of_deposit+1)):
    percent_of_start = (start * persent)/100 
    start = start + percent_of_start + replenishment_amount
    
    print("Год:" , i, ", "  "накоплено с учетом процента на остаток: ", start)

print("Дата выхода на 'пенсию'", age + term_of_deposit)
print("Каждый месяц вы можете свободно снимать: ", start / 12 / time_of_luxury)
