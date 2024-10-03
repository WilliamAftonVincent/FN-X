
import os
import subprocess
import socket

# Создание папки FN-X, если она не существует
if not os.path.exists("FN-X"):
    os.makedirs("FN-X")

def change_directory(path):
    try:
        os.chdir(path)
    except FileNotFoundError:
        print(f"Папка не найдена: {path}")

def list_files():
    files = os.listdir()
    for file in files:
        print(file)

def edit_file(filename):
    if os.path.exists(filename):
        subprocess.call(['nano', filename])
    else:
        print(f"Файл не найден: {filename}")

def current_directory():
    print(os.getcwd())

def remove_file_or_dir(path):
    try:
        if os.path.isfile(path):
            os.remove(path)
        elif os.path.isdir(path):
            os.rmdir(path)  # Удаляет пустую папку, для удаления непустой нужно использовать shutil.rmtree
        else:
            print(f"Не найден файл или каталог: {path}")
    except Exception as e:
        print(f"Ошибка: {e}")

def create_directory(name):
    try:
        os.makedirs(name)
    except FileExistsError:
        print(f"Папка уже существует: {name}")

def install_package(package):
    subprocess.call(['sudo', 'apt-get', 'install', package])  # Пример для Debian/Ubuntu

def remove_package(package):
    subprocess.call(['sudo', 'apt-get', 'remove', package])  # Пример для Debian/Ubuntu

def update_packages():
    subprocess.call(['sudo', 'apt-get', 'update'])  # Обновляет индекс пакетов

def upgrade_packages():
    subprocess.call(['sudo', 'apt-get', 'upgrade'])  # Обновляет установленные пакеты

def reboot_system():
    subprocess.call(['sudo', 'reboot'])  # Перезагружает систему

def poweroff_system():
    subprocess.call(['sudo', 'poweroff'])  # Выключает систему

def download_file(url):
    subprocess.call(['wget', url])  # Загружает файл из интернета

def my_ip():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    print(f"Ваш IP адрес: {ip_address}")

def main():
    while True:
        command = input(f"FN-X:{os.getcwd()} $ ").strip().split()
        cmd_name = command[0]

        if cmd_name == "td":  # cd
            change_directory(" ".join(command[1:]))
        elif cmd_name == "dfl":  # ls
            list_files()
        elif cmd_name == "eaf":  # nano
            edit_file(" ".join(command[1:]))
        elif cmd_name == "cdp":  # выводит полный путь текущей директории
            current_directory()
        elif cmd_name == "del":  # удаление файла или каталога
            remove_file_or_dir(" ".join(command[1:]))
        elif cmd_name == "cf":  # создание нового каталога
            create_directory(" ".join(command[1:]))
        elif cmd_name == "install":  # установка пакета
            install_package(" ".join(command[1:]))
        elif cmd_name == "remove":  # удаление пакета
            remove_package(" ".join(command[1:]))
        elif cmd_name == "update":  # обновление списка пакетов
            update_packages()
        elif cmd_name == "upgrade":  # обновление пакетов
            upgrade_packages()
        elif cmd_name == "reboot":  # перезагрузка
            reboot_system()
        elif cmd_name == "poweroff":  # выключение
            poweroff_system()
        elif cmd_name == "dfn":  # скачивание файла
            download_file(" ".join(command[1:]))
        elif cmd_name == "myip":  # получение IP
            my_ip()
        elif cmd_name == "exit":
            break
        else:
            print("Неизвестная команда")

if __name__ == "__main__":
    main()