import paramiko
import ftplib
import os

def upload_sftp(server, username, password, local_file, remote_path):
    """Загружает файл на удалённый сервер через SFTP."""
    transport = paramiko.Transport((server, 22))
    transport.connect(username=username, password=password)
    sftp = transport.open_sftp()
    sftp.put(local_file, remote_path)
    sftp.close()
    transport.close()
    print(f"Файл {local_file} загружен на {server}:{remote_path}")

def upload_ftp(server, username, password, local_file, remote_path):
    """Загружает файл на FTP-сервер."""
    with ftplib.FTP(server, username, password) as ftp, open(local_file, "rb") as file:
        ftp.storbinary(f"STOR {remote_path}", file)
        print(f"Файл {local_file} загружен на FTP {server}")

if __name__ == "__main__":
    method = input("Выберите метод (sftp/ftp): ").strip().lower()
    server = input("Введите сервер: ")
    username = input("Введите логин: ")
    password = input("Введите пароль: ")
    local_file = input("Введите путь к файлу: ")
    remote_path = input("Введите путь на сервере: ")

    if method == "sftp":
        upload_sftp(server, username, password, local_file, remote_path)
    elif method == "ftp":
        upload_ftp(server, username, password, local_file, remote_path)
    else:
        print("Ошибка: неверный метод.")
