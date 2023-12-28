import os


class FileManager:
    # Метод для просмотра содержимого текущей директории
    def view_directory(self):
        current_dir = os.getcwd()  # Получаем путь к текущей директории
        files = os.listdir(current_dir)  # Получаем список файлов и директорий в текущей директории
        for file in files:
            print(file)

    # Метод для создания новой директории
    def create_directory(self, dir_name):
        os.mkdir(dir_name)
        print(f"Директория {dir_name} создана успешно")

    # Метод для удаления директории или файла
    def delete(self, path):
        if os.path.isdir(path):
            os.rmdir(path)
            print(f"Директория {path} удалена успешно")
        elif os.path.isfile(path):
            os.remove(path)
            print(f"Файл {path} удален успешно")

    # Метод для копирования файла или директории
    def copy(self, source, destination):
        if os.path.isdir(source):
            os.makedirs(destination)
            for root, dirs, files in os.walk(source):
                for file in files:
                    src_file = os.path.join(root, file)
                    dest_file = os.path.join(destination, file)
                    with open(src_file, 'rb') as fsrc, open(dest_file, 'wb') as fdest:
                        fdest.write(fsrc.read())
            print(f"Директория {source} скопирована в {destination} успешно")
        elif os.path.isfile(source):
            with open(source, 'rb') as fsrc, open(destination, 'wb') as fdest:
                fdest.write(fsrc.read())
            print(f"Файл {source} скопирован в {destination} успешно")

    # Метод для перемещения файла или директории
    def move(self, source, destination):
        os.rename(source, destination)
        print(f"Успешно перемещено из {source} в {destination}")

        # Метод для поиска файла по имени в текущей директории и поддиректориях
        def search_file(self, filename, current_dir):
            for root, dirs, files in os.walk(current_dir):
                if filename in files:
                    print(f"Файл {filename} найден в {root}")

                    # Метод для изменения прав доступа к файлу или директории
                    def change_permissions(self, path, mode):
                        os.chmod(path, mode)
                        print(f"Права доступа к {path} изменены успешно")

            #Пример:

            file_manager = FileManager()

            # Просмотр содержимого текущей директории
            file_manager.view_directory()

            # Создание новой директории
            file_manager.create_directory("new_directory")

            # Удаление директории или файла
            file_manager.delete("directory_to_delete")
            file_manager.delete("file_to_delete.txt")

            # Копирование файла или директории
            file_manager.copy("source_dir", "destination_dir")
            file_manager.copy("source_file.txt", "destination_file.txt")

            # Перемещение файла или директории
            file_manager.move("source_dir", "destination_dir")
            file_manager.move("source_file.txt", "destination_file.txt")

            # Поиск файла по имени в текущей директории и поддиректориях
            file_manager.search_file("filename.txt", os.getcwd())

            # Изменение прав доступа к файлу или директории
            file_manager.change_permissions("file.txt", 0o755)