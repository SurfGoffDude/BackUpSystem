import sys
import os


def resource_path(relative_path):
    """ Получаем путь к ресурсам внутри исполняемого файла """
    if getattr(sys, '_MEIPASS', False):  # Проверяем, существует ли _MEIPASS
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath(os.path.dirname(__file__))  # ✅ cx_Freeze-friendly путь
    return os.path.join(base_path, relative_path)


# ✅ Добавляем путь к backup_app ПЕРЕД импортами
sys.path.append(resource_path("backup_app"))

from PyQt6.QtWidgets import QApplication
from backup_app.ui.main_window import MainWindow
from backup_app.config.settings import load_settings
from backup_app.logs.logger import log_info


def setup_app():
    """Готовит окружение приложения"""
    base_dir = resource_path("backup_app")  # ✅ Указываем правильную папку

    for folder in ["logs", "backups", "config"]:
        full_path = os.path.join(base_dir, folder)
        if not os.path.exists(full_path):
            os.makedirs(full_path)

    settings = load_settings()
    log_info("Настройки загружены.")

    return settings


if __name__ == "__main__":
    settings = setup_app()

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    log_info("Приложение запущено.")

    sys.exit(app.exec())
