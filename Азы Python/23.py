#Класс
class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(restaurant_name, cuisine_type, number_served = 0 ):
        print('Название ресторана - ', restaurant_name,',','Тип кухни - ',  cuisine_type, 'Обслужино клиентов - ', number_served)

    def open_restaurant(open_close):
        print('Ресторан - ' + open_close)

    def increment_number_served(number):
        numberNew =+ number
        print('Всего клиентов: ', numberNew)

#Первая часть
print('\nПервая часть')
my_restaurant = Restaurant.describe_restaurant('Галера', 'Вегетарианская кухня', 5)
my_restaurant_info = Restaurant.open_restaurant('Открыт')
my_restaurant_guests = Restaurant.increment_number_served(8)

#Новый класс

class User():
    def greet_user(first_name , last_name, info = 'Nothing info'):
        print('Имя - ', first_name, ',', 'Фамилия - ', last_name, ',', 'Другая информация - ', info)

    def increment_login_attempts(login_attempts ):
        login_attempts +=1
        print('Инкремент = ', login_attempts )

    def reset_login_attempts(login_attempts):
        login_attempts = 0
        print('Сброс значения = ', login_attempts)

    #Вторая часть
print('\nВторая часть')
new_user_increment = User.increment_login_attempts(3)
new_user_increment2 = User.reset_login_attempts(2)