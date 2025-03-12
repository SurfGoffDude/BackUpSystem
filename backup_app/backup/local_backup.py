import os
import shutil
from datetime import datetime
from backup_app.logs.logger import log_info, log_error

BACKUP_DIR = os.path.expanduser("~/Downloads/backups/")

os.makedirs(BACKUP_DIR, exist_ok=True)


def create_backup(source_path):
    """Создаёт резервную копию файла или папки в новой структуре."""
    if not os.path.exists(source_path):
        log_error(f"Ошибка: {source_path} не найден!")
        return False

    file_name = os.path.basename(source_path)  # Получаем только имя файла
    today = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    backup_folder = os.path.join(BACKUP_DIR, file_name, today)  # 🗂️ Новый путь хранения
    os.makedirs(backup_folder, exist_ok=True)

    destination = os.path.join(backup_folder, file_name)
    log_info(f"📄 Копируем {source_path} -> {destination}")
    shutil.copy2(source_path, destination)

    log_info(f"✅ Бэкап завершён: {destination}")
    return destination
