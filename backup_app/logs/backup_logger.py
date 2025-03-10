import logging
import os

LOG_DIR = "logs"
BACKUP_LOG_FILE = os.path.join(LOG_DIR, "backup.log")

if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler(BACKUP_LOG_FILE, encoding="utf-8")]
)

def log_backup_success(backup_file, size_mb, duration):
    """Логирует успешное создание бэкапа"""
    logging.info(f"✅ Бэкап {backup_file} ({size_mb:.2f} MB) создан за {duration:.2f} сек.")

def log_backup_error(backup_file, error_message):
    """Логирует ошибку при создании бэкапа"""
    logging.error(f"❌ Ошибка при создании {backup_file}: {error_message}")

if __name__ == "__main__":
    log_backup_success("backup_2024-03-10.tar.gz", 250.5, 10.2)
    log_backup_error("backup_2024-03-10.tar.gz", "Недостаточно места на диске")
