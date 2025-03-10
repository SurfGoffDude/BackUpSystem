import logging
import os

LOG_DIR = "logs"
LOG_FILE = os.path.join(LOG_DIR, "app.log")

if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE, encoding="utf-8"),
        logging.StreamHandler()
    ]
)

def log_info(message):
    """Записывает информационное сообщение в лог"""
    logging.info(message)

def log_warning(message):
    """Записывает предупреждение в лог"""
    logging.warning(message)

def log_error(message):
    """Записывает ошибку в лог"""
    logging.error(message)

if __name__ == "__main__":
    log_info("Приложение запущено.")
    log_warning("Тестовое предупреждение.")
    log_error("Тестовая ошибка.")
