import os
import tarfile

BACKUP_DIR = "backups/"

def restore_backup(backup_file, restore_path):
    """Разархивирует бэкап в указанную папку."""
    if not os.path.exists(backup_file):
        raise FileNotFoundError(f"Файл {backup_file} не найден.")

    with tarfile.open(backup_file, "r:gz") as tar:
        tar.extractall(path=restore_path)

    print(f"Бэкап {backup_file} восстановлен в {restore_path}")

if __name__ == "__main__":
    backup_file = input("Введите путь к бэкапу: ")
    restore_path = input("Введите путь для восстановления: ")
    restore_backup(backup_file, restore_path)
