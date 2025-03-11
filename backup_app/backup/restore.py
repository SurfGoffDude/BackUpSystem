import os
import shutil
from datetime import datetime
from backup_app.logs.logger import log_info, log_error

BACKUP_DIR = os.path.expanduser("~/Downloads/backups/")


def find_latest_backup(file_name):
    """Ищет последнюю версию файла в ~/Downloads/backups/{имя файла}/{дата}/файл."""
    file_backup_path = os.path.join(BACKUP_DIR, file_name)

    if not os.path.exists(file_backup_path) or not os.path.isdir(file_backup_path):
        log_error(f"❌ Папка {file_backup_path} не найдена или это не директория!")
        return None

    # 🔥 Теперь сортируем только папки с датами, исключая файлы
    backup_folders = sorted(
        [f for f in os.listdir(file_backup_path) if os.path.isdir(os.path.join(file_backup_path, f))],
        reverse=True
    )

    if not backup_folders:
        log_error(f"❌ В папке {file_backup_path} нет бэкапов!")
        return None

    for folder in backup_folders:
        backup_file = os.path.join(file_backup_path, folder, file_name)
        if os.path.isfile(backup_file):
            log_info(f"✅ Найден бэкап: {backup_file}")
            return backup_file

    log_error(f"❌ Файл {file_name} не найден в ~/Downloads/backups/{file_name}/.")
    return None


def find_all_backups(file_name):
    """Находит ВСЕ версии файла в ~/Downloads/backups/{имя файла}/{дата}/файл."""
    file_backup_path = os.path.join(BACKUP_DIR, file_name)

    if not os.path.exists(file_backup_path) or not os.path.isdir(file_backup_path):
        log_error(f"❌ Папка {file_backup_path} не найдена!")
        return []

    # 🔥 Теперь собираем ВСЕ версии файла
    backup_versions = [
        os.path.join(file_backup_path, folder, file_name)
        for folder in sorted(os.listdir(file_backup_path), reverse=True)
        if os.path.isdir(os.path.join(file_backup_path, folder))
    ]

    if not backup_versions:
        log_error(f"❌ В папке {file_backup_path} нет бэкапов!")
    return backup_versions


def restore_backup(file_name, restore_base_path):
    """Восстанавливает файл из последнего бэкапа в ~/Downloads/Restore/{имя файла}/{дата}/файл."""
    backup_file = find_latest_backup(file_name)

    if not backup_file:
        log_error(f"❌ Ошибка восстановления! Файл {file_name} не найден в backups/")
        return False

    # 📅 Получаем дату последнего изменения файла
    modified_time = os.path.getmtime(backup_file)
    formatted_date = datetime.fromtimestamp(modified_time).strftime("%Y-%m-%d_%H-%M-%S")

    # ✅ Проверяем, нет ли уже `file_name` в `restore_base_path`
    if os.path.basename(restore_base_path) == file_name:
        final_restore_path = os.path.join(restore_base_path, formatted_date)
    else:
        final_restore_path = os.path.join(restore_base_path, formatted_date)

        # ✅ Проверяем, не является ли `final_restore_path` файлом
    if os.path.exists(final_restore_path) and not os.path.isdir(final_restore_path):
        log_error(f"❌ Ошибка: {final_restore_path} уже существует и это не папка!")
        return False

    os.makedirs(final_restore_path, exist_ok=True)  # ✅ Создаём папку, если её нет

    restored_file_path = os.path.join(final_restore_path, file_name)
    shutil.copy2(backup_file, restored_file_path)

    log_info(f"✅ Файл {file_name} восстановлен в {final_restore_path}")
    return restored_file_path


def restore_all_files(restore_base_path):
    """Восстанавливает ВСЕ версии ВСЕХ файлов из ~/Downloads/backups/{имя файла}/{дата}/файл."""
    if not os.path.exists(BACKUP_DIR):
        log_error(f"❌ Папка {BACKUP_DIR} не существует!")
        return False

    restored_files = []

    file_folders = [f for f in os.listdir(BACKUP_DIR) if os.path.isdir(os.path.join(BACKUP_DIR, f))]

    if not file_folders:
        log_error(f"❌ В папке ~/Downloads/backups/ нет файлов для восстановления!")
        return False

    for file_name in file_folders:
        file_backup_path = os.path.join(BACKUP_DIR, file_name)

        if not os.path.isdir(file_backup_path):
            log_error(f"⚠ Пропускаем {file_backup_path}, так как это не папка")
            continue

        all_versions = find_all_backups(file_name)

        for backup_file in all_versions:
            modified_time = os.path.getmtime(backup_file)
            formatted_date = datetime.fromtimestamp(modified_time).strftime("%Y-%m-%d_%H-%M-%S")

            # 🔥 Убираем лишние уровни вложенности
            restore_path = os.path.join(restore_base_path, file_name, formatted_date)

            if os.path.exists(restore_path) and not os.path.isdir(restore_path):
                log_error(f"❌ Ошибка: {restore_path} уже существует и это не папка!")
                continue

            os.makedirs(restore_path, exist_ok=True)

            restored_file = restore_backup(file_name, restore_path)
            if restored_file:
                restored_files.append(restored_file)

    if restored_files:
        log_info(f"✅ Восстановлены ВСЕ файлы: {restored_files}")
        return restored_files
    else:
        log_error(f"❌ В папке ~/Downloads/backups/ нет доступных файлов для восстановления!")
        return False
