#Класс
class Restaurant():
    def __init__(self, restaurant_name, cuisine_type ):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(restaurant_name, cuisine_type):
        print('Название ресторана - ', restaurant_name,',','Тип кухни - ',  cuisine_type)

    def open_restaurant(open_close):
        print('Ресторан - ' + open_close)

#Первая часть
print('\nПервая часть')
my_restaurant = Restaurant.describe_restaurant('Галера', 'Вегетарианская кухня')
my_restaurant_info = Restaurant.open_restaurant('Открыт')

#Вторая часть
print('\nВторая часть')
my_restaurant2 = Restaurant.describe_restaurant('Мяу', 'Мурмяшья кухня')
my_restaurant3 = Restaurant.describe_restaurant('Вася', 'Японская кухня')
my_restaurant4 = Restaurant.describe_restaurant('Молоко', 'Азиатская кухня')

#Новый класс

class User():
    def greet_user(first_name , last_name, info = 'Nothing info'):
        print('Имя - ', first_name, ',', 'Фамилия - ', last_name, ',', 'Другая информация - ', info)

#Третья часть
print('\nТретья часть')
new_user = User.greet_user('AnLi','Man')
new_user2 = User.greet_user('Саня','Мурзякин', 'Отшкурьенный')