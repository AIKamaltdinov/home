with open('file.xml', 'r', encoding='utf-8') as file: # открываем файл file.xml для чтения
    lines = file.readlines() # считываем все строки из файла
c = 0 # переменная для подсчета количества ссылок

for line in lines: # проходим по каждой строке
    if 'http' in line: # если в строке есть подстрока ‘http’
         end_link = 0 # переменная для хранения индекса конца ссылки

while line.find('http', end_link) != -1: # пока не найдены все ссылки в строке
    start_link = line.find('http', end_link) # находим индекс начала ссылки

# находим возможные концы ссылок
if line[start_link - 1] == '"':
    end_link = line.find('"', start_link) # если конец ссылки - кавычка, то находим индекс этой кавычки
elif line[start_link - 1] == '':
    end_link = line.find('', start_link) # если конец ссылки - пробел, то находим индекс этого пробела
else:
    end_link = line.rfind('<') # в остальных случаях конец ссылки - символ ‘<’

c += 1 # увеличиваем счетчик ссылок
print(line[start_link:end_link]) # выводим найденную ссылку

print('\nВсего ссылок найдено: ', c) # выводим общее количество найденных ссылок