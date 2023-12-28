# Создаем класс Товар
class Product:
    def init(self, name, id, price, rating, stock):
        self.name = name  # переменная для имени товара
        self.id = id  # переменная для идентификатора товара
        self.price = price  # переменная для цены товара
        self.rating = rating  # переменная для рейтинга товара
        self.stock = stock  # переменная для количества доступных товаров

    def add_stock(self, quantity):
        self.stock += quantity  # увеличиваем количество доступных товаров на заданную величину

    def remove_stock(self, quantity):
        self.stock -= quantity  # уменьшаем количество доступных товаров на заданную величину

    def update_rating(self, new_rating):
        self.rating = new_rating  # обновляем рейтинг товара

    def update_price(self, new_price):
        self.price = new_price  # обновляем цену товара


# Создаем класс Категория
class Category:
    def init(self, name):
        self.name = name  # переменная для имени категории
        self.items = []  # переменная для списка товаров в категории

    def add_item(self, item):
        self.items.append(item)  # добавляем товар в список товаров категории

    def remove_item(self, item):
        self.items.remove(item)  # удаляем товар из списка товаров категории

    def get_item(self, id):
        for item in self.items:
            if item.id == id:
                return item  # возвращаем товар по заданному идентификатору


# Создаем класс Basket
class Basket:
    def init(self):
        self.items = []  # переменная для списка товаров в корзине

    def add_item(self, item):
        self.items.append(item)  # добавляем товар в список товаров корзины

    def remove_item(self, item):
        self.items.remove(item)  # удаляем товар из списка товаров корзины

    def get_item(self, id):
        for item in self.items:
            if item.id == id:
                return item  # возвращаем товар по заданному идентификатору

    def make_purchase(self, item_ids):
        purchased_items = []
        for item_id in item_ids:
            for item in self.items:
                if item.id == item_id:
                    purchased_items.append(item)  # добавляем купленный товар в список
                    self.items.remove(item)  # удаляем купленный товар из списка корзины
                    break
        for item in purchased_items:
            print(item.name)  # выводим на консоль названия купленных товаров


# Создаем класс User
class User:
    def init(self, login, password):
        self.login = login  # переменная для логина пользователя
        self.password = password  # переменная для пароля пользователя
        self.basket = Basket()  # создаем объект корзины для пользователя