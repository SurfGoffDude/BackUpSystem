import os
import shutil
from datetime import datetime
from backup_app.logs.logger import log_info, log_error

BACKUP_DIR = "backups/"


def create_backup(source_path):
    """Создаёт резервную копию файла или папки."""
    if not os.path.exists(source_path):
        log_error(f"Ошибка: {source_path} не найден!")
        return False

    today = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    backup_folder = os.path.join(BACKUP_DIR, today)

    if not os.path.exists(backup_folder):
        os.makedirs(backup_folder)

    if os.path.isdir(source_path):
        log_info(f"📂 Копируем папку {source_path} -> {backup_folder}")
        shutil.copytree(source_path, os.path.join(backup_folder, os.path.basename(source_path)))
    else:
        destination = os.path.join(backup_folder, os.path.basename(source_path))  # ✅ Теперь путь к файлу
        log_info(f"📄 Копируем файл {source_path} -> {destination}")
        shutil.copy2(source_path, destination)

    log_info(f"✅ Бэкап завершён: {backup_folder}")
    return backup_folder
