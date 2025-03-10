import os
import shutil
from logs.logger import log_info, log_error
from ui.notifications import send_notification

BACKUP_DIR = "backups/"

def find_latest_backup(file_name):
    """Ищет последнюю версию файла в бэкапах."""
    backup_folders = sorted(os.listdir(BACKUP_DIR), reverse=True)  # Берём самые новые папки
    for folder in backup_folders:
        backup_path = os.path.join(BACKUP_DIR, folder, file_name)
        if os.path.isfile(backup_path):
            return backup_path
    return None  # Если файла нет в бэкапах

def restore_backup(file_name, restore_path):
    """Восстанавливает файл из последнего бэкапа."""
    backup_file = find_latest_backup(file_name)

    if not backup_file:
        log_error(f"Файл {file_name} не найден в бэкапах.")
        send_notification("Ошибка восстановления", f"Файл {file_name} отсутствует в резервных копиях.")
        return False

    if not os.path.exists(restore_path):
        os.makedirs(restore_path)

    restored_file_path = os.path.join(restore_path, file_name)
    shutil.copy2(backup_file, restored_file_path)

    log_info(f"✅ Файл {file_name} восстановлен в {restore_path}")
    send_notification("Восстановление завершено", f"Файл сохранён в {restore_path}")

    return restored_file_path
