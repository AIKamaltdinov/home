import re

# Функция для поиска слов в строке
def srh_word(string):
    return re.findall(pattern=r'\b[-a-zA-Zа-яА-ЯёЁ]+\b', string=string)

def main():
    put = input()  # получение ввода от пользователя

    mch = srh_word(put) # нахождение слов в строке

    print(len(mch)) # вывод количества найденных слов

if __name__ == '__main__':
    main() # вызов основной функции