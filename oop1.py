class Book:
    # Конструктор класса, инициализирует переменные при создании объекта
    def init(self, title, author, year, pages):
        self.title = title  # переменная, хранящая название книги
        self.author = author  # переменная, хранящая автора книги
        self.year = year  # переменная, хранящая год издания книги
        self.pages = pages  # переменная, хранящая количество страниц книги

    # Метод для вывода информации о книге
    def display_info(self):
        print(f"Название: {self.title}")
        print(f"Автор: {self.author}")
        print(f"Год издания: {self.year}")
        print(f"Количество страниц: {self.pages}")

        # Метод для изменения количества страниц книги
        def change_pages(self, new_pages):
            self.pages = new_pages

        # Метод для вывода информации о книге в формате строки
        def str(self):
            return f"Название: {self.title}, автор: {self.author}, год издания: {self.year}, количество страниц: {self.pages}"

    #Пример создания и использования экземпляров класса:

# Создание объектов класса Книга
book1 = Book("Kniga1", "Avlor1", 0, 1000)
book2 = Book("Kniga2", "Avtor2", 2077, 1)

# Вывод информации о книгах
book1.display_info()
book2.display_info()

# Изменение количества страниц книги
book1.change_pages(9999)

# Вывод информации о книгах в формате строки
print(book1)
print(book2)