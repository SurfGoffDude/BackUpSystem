import os
import shutil
from logs.logger import log_info, log_error
from ui.notifications import send_notification

BACKUP_DIR = "backups/"

def restore_backup(backup_file, restore_path):
    """Восстанавливает файл из указанной папки бэкапа."""
    if not os.path.exists(backup_file):
        log_error(f"Файл {backup_file} не найден в бэкапе.")
        send_notification("Ошибка восстановления", f"Файл {backup_file} не найден.")
        return False

    if not os.path.exists(restore_path):
        os.makedirs(restore_path)

    restored_file_path = os.path.join(restore_path, os.path.basename(backup_file))
    shutil.copy2(backup_file, restored_file_path)

    log_info(f"✅ Файл {backup_file} восстановлен в {restore_path}")
    send_notification("Восстановление завершено", f"Файл сохранён в {restore_path}")

    return restored_file_path
