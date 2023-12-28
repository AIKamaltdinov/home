import re

# Функция для поиска строк, соответствующих формату номера частного легкового автомобиля
def srh_pr(string):
    return re.findall(pattern=r'\b[АВЕКМНОРСKMHOPCTY]\d{3}[АВЕКМНОРСТУХABEKMHOPCТУХABETY]{2}\d{2,3}\b', string=string)

# Функция для поиска строк, соответствующих формату номера такси
def srh_tx(string):
    return re.findall(pattern=r'\b[АВЕКТУХABEХABEKMHY]{2}\d{5,6}\b', string=string)

# Функция, которая сопоставляет каждую строку с найденными номерами и определяет тип номера
def maches(string, private, taxi):
    ret_string = ''
    for num in string.split(): # разделяем строку на отдельные слова
        if num in private: # если слово найдено среди номеров частного легкового автомобиля
            ret_string += 'Частный'
        elif num in taxi: # если слово найдено среди номеров такси
            ret_string += 'Такси'
        else: # если слово не найдено в номерах
            ret_string += 'Не номер'

    return ret_string

def main():
    put = input() # ввод строки

# Находим номера частных легковых автомобилей и такси
    mch_private = srh_pr(put)
    mch_taxi = srh_tx(put)

# Определяем тип номера для каждого слова в строке и выводим результат
    print(maches(put, mch_private, mch_taxi))

if __name__ == 'main':
    main()