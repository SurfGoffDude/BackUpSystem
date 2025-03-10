import os
import shutil
import subprocess
from datetime import datetime

BACKUP_BASE_DIR = "backups/"

def create_time_machine_backup(source_folder):
    """Создаёт инкрементный бэкап, сохраняя историю версий."""
    if not os.path.exists(source_folder):
        raise FileNotFoundError(f"Папка {source_folder} не найдена.")

    today = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    new_backup_path = os.path.join(BACKUP_BASE_DIR, today)

    backups = sorted(os.listdir(BACKUP_BASE_DIR))
    previous_backup = os.path.join(BACKUP_BASE_DIR, backups[-1]) if backups else None

    rsync_command = [
        "rsync", "-a", "--delete",
        "--link-dest=" + previous_backup if previous_backup else "",
        source_folder + "/", new_backup_path
    ]

    subprocess.run(" ".join(rsync_command), shell=True, check=True)
    print(f"✅ Бэкап создан: {new_backup_path}")

    return new_backup_path
