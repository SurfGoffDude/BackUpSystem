import logging
import os

LOG_DIR = "logs"
CLOUD_LOG_FILE = os.path.join(LOG_DIR, "cloud.log")

if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler(CLOUD_LOG_FILE, encoding="utf-8")]
)

def log_cloud_upload(service, file_name, status, speed=None):
    """Логирует загрузку файла в облако"""
    if status == "success":
        logging.info(f"✅ {file_name} успешно загружен в {service} (Скорость: {speed:.2f} MB/s)")
    else:
        logging.error(f"❌ Ошибка загрузки {file_name} в {service}")

if __name__ == "__main__":
    log_cloud_upload("Google Drive", "backup_2024-03-10.tar.gz", "success", speed=5.2)
    log_cloud_upload("Amazon S3", "backup_2024-03-10.tar.gz", "error")
