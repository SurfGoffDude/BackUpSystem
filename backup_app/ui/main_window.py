from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QTextEdit, QVBoxLayout, QWidget
from backup_app.ui.settings_window import SettingsWindow
from backup_app.ui.widgets import DragDropWidget
from backup_app.backup.restore import restore_backup
from backup_app.backup.local_backup import create_backup
import sys
import os


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Backup Manager")
        self.setGeometry(300, 200, 600, 400)

        self.selected_folder = None

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.log = QTextEdit()
        self.log.setReadOnly(True)

        self.drag_drop_widget = DragDropWidget(self)

        self.backup_button = QPushButton("🚀 Создать бэкап")
        self.backup_button.setEnabled(False)
        self.backup_button.clicked.connect(self.create_backup)

        self.restore_button = QPushButton("🔄 Восстановить")
        self.restore_button.setEnabled(False)
        self.restore_button.clicked.connect(self.restore_backup)

        self.settings_button = QPushButton("⚙️ Настройки")  # 🔥 Вернули кнопку!
        self.settings_button.clicked.connect(self.open_settings)

        layout = QVBoxLayout()
        layout.addWidget(self.drag_drop_widget)
        layout.addWidget(self.backup_button)
        layout.addWidget(self.restore_button)
        layout.addWidget(self.settings_button)  # 🔥 Убедились, что кнопка есть!
        layout.addWidget(self.log)
        self.central_widget.setLayout(layout)

    def create_backup(self):
        if self.selected_folder:
            backup_path = create_backup(self.selected_folder)

            if backup_path:
                self.log.append(f"✅ Бэкап создан: {backup_path}")
            else:
                self.log.append("❌ Ошибка при создании бэкапа")
        else:
            self.log.append("❌ Ошибка: выберите файл или папку для бэкапа")

    def restore_backup(self):
        if self.selected_folder:
            file_name = os.path.basename(self.selected_folder)
            restore_path = os.path.expanduser("~/Downloads/Restore")
            restored_file = restore_backup(file_name, restore_path)

            if restored_file:
                self.log.append(f"✅ Файл восстановлен: {restored_file}")
            else:
                self.log.append(f"❌ Ошибка восстановления! Проверьте содержимое backups/!")
        else:
            self.log.append("❌ Ошибка: выберите файл для восстановления")

    def open_settings(self):
        self.settings_window = SettingsWindow()
        self.settings_window.show()
