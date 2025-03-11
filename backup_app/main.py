import sys
import os
from PyQt6.QtWidgets import QApplication
from ui.main_window import MainWindow
from config.settings import load_settings
from logs.logger import log_info


def setup_app():
    """Готовит окружение приложения"""
    for folder in ["logs", "backups", "config"]:
        if not os.path.exists(folder):
            os.makedirs(folder)

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
