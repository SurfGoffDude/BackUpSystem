import os
import shutil
from backup_app.logs.logger import log_info, log_error
from backup_app.ui.notifications import send_notification

BACKUP_DIR = "backups/"


def find_latest_backup(file_name):
    """Ищет последнюю версию файла в папке backups/."""
    if not os.path.exists(BACKUP_DIR):
        log_error(f"Папка {BACKUP_DIR} не существует!")
        return None

    backup_folders = sorted(os.listdir(BACKUP_DIR), reverse=True)  # Сортируем по времени
    log_info(f"🔍 Проверяем бэкапы: {backup_folders}")

    for folder in backup_folders:
        backup_path = os.path.join(BACKUP_DIR, folder, file_name)
        if os.path.isfile(backup_path):
            log_info(f"✅ Файл найден в {backup_path}")
            return backup_path

    log_error(f"❌ Файл {file_name} не найден в папке backups/!")
    return None  # Если файл не найден


def restore_backup(file_name, restore_path):
    """Восстанавливает файл из последнего бэкапа."""
    backup_file = find_latest_backup(file_name)

    if not backup_file:
        send_notification("Ошибка восстановления", f"Файл {file_name} отсутствует в бэкапах!")
        return False

    if not os.path.exists(restore_path):
        os.makedirs(restore_path)

    restored_file_path = os.path.join(restore_path, file_name)
    shutil.copy2(backup_file, restored_file_path)

    log_info(f"✅ Файл {file_name} восстановлен в {restore_path}")
    send_notification("Восстановление завершено", f"Файл сохранён в {restore_path}")

    return restored_file_path
