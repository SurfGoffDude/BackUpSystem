from cryptography.fernet import Fernet

KEY_FILE = "backup.key"


def generate_key():
    """Генерирует и сохраняет ключ для шифрования."""
    key = Fernet.generate_key()
    with open(KEY_FILE, "wb") as file:
        file.write(key)
    print("Ключ сохранён в", KEY_FILE)


def load_key():
    """Загружает ключ из файла."""
    with open(KEY_FILE, "rb") as file:
        return file.read()


def encrypt_file(filename):
    """Шифрует файл."""
    key = load_key()
    cipher = Fernet(key)

    with open(filename, "rb") as file:
        encrypted_data = cipher.encrypt(file.read())

    with open(filename + ".enc", "wb") as file:
        file.write(encrypted_data)

    print(f"Файл {filename} зашифрован.")


def decrypt_file(encrypted_filename):
    """Расшифровывает файл."""
    key = load_key()
    cipher = Fernet(key)

    with open(encrypted_filename, "rb") as file:
        decrypted_data = cipher.decrypt(file.read())

    original_filename = encrypted_filename.replace(".enc", "")

    with open(original_filename, "wb") as file:
        file.write(decrypted_data)

    print(f"Файл {encrypted_filename} расшифрован в {original_filename}")


if __name__ == "__main__":
    action = input("Выберите действие (generate/encrypt/decrypt): ").strip().lower()
    if action == "generate":
        generate_key()
    elif action == "encrypt":
        filename = input("Введите путь к файлу: ")
        encrypt_file(filename)
    elif action == "decrypt":
        filename = input("Введите путь к зашифрованному файлу: ")
        decrypt_file(filename)
    else:
        print("Ошибка: неверная команда.")
