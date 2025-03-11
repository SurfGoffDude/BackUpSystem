import os
import shutil
from datetime import datetime
from backup_app.logs.logger import log_info, log_error

BACKUP_DIR = "backups/"


def find_latest_backup(file_name):
    """Ищет последнюю версию файла в новой структуре backups/{имя файла}/{дата}/файл."""
    file_backup_path = os.path.join(BACKUP_DIR, file_name)

    if not os.path.exists(file_backup_path):
        log_error(f"❌ Папка {file_backup_path} не найдена!")
        return None

    backup_folders = sorted(os.listdir(file_backup_path), reverse=True)  # Сортируем по дате
    for folder in backup_folders:
        backup_file = os.path.join(file_backup_path, folder, file_name)
        if os.path.isfile(backup_file):
            log_info(f"✅ Найден бэкап: {backup_file}")
            return backup_file

    log_error(f"❌ Файл {file_name} не найден в backups/{file_name}/")
    return None  # Если файл не найден


def restore_backup(file_name, restore_base_path):
    """Восстанавливает файл из последнего бэкапа в ~/Downloads/Restore/{имя файла}/{дата}/файл."""
    backup_file = find_latest_backup(file_name)

    if not backup_file:
        log_error(f"❌ Ошибка восстановления! Файл {file_name} не найден в backups/")
        return False

    # 📅 Получаем дату последнего изменения файла
    modified_time = os.path.getmtime(backup_file)
    formatted_date = datetime.fromtimestamp(modified_time).strftime("%Y-%m-%d_%H-%M-%S")

    # 🗂️ Новый путь восстановления (исключаем лишние уровни вложенности)
    final_restore_path = os.path.join(restore_base_path, file_name, formatted_date)

    if os.path.basename(final_restore_path) == file_name:
        final_restore_path = os.path.join(restore_base_path, formatted_date)  # Убираем дублирование

    os.makedirs(final_restore_path, exist_ok=True)

    restored_file_path = os.path.join(final_restore_path, file_name)
    shutil.copy2(backup_file, restored_file_path)

    log_info(f"✅ Файл {file_name} восстановлен в {final_restore_path}")
    return restored_file_path


def restore_all_files(restore_base_path):
    """Восстанавливает все файлы из backups/."""
    if not os.path.exists(BACKUP_DIR):
        log_error(f"❌ Папка {BACKUP_DIR} не существует!")
        return False

    restored_files = []
    for folder in os.listdir(BACKUP_DIR):
        folder_path = os.path.join(BACKUP_DIR, folder)
        if os.path.isdir(folder_path):  # Проверяем, что это папка
            for file_name in os.listdir(folder_path):
                backup_file = os.path.join(folder_path, file_name)
                if os.path.isfile(backup_file):
                    restored_file = restore_backup(file_name, restore_base_path)
                    if restored_file:
                        restored_files.append(restored_file)

    if restored_files:
        log_info(f"✅ Восстановлены все файлы: {restored_files}")
        return restored_files
    else:
        log_error(f"❌ В папке backups/ нет файлов для восстановления")
        return False
