from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QTextEdit, QVBoxLayout, QWidget, QFileDialog
from backup_app.ui.widgets import DragDropWidget
from backup_app.backup.local_backup import create_backup
from backup_app.backup.restore import restore_backup, find_latest_backup, restore_all_files
from backup_app.logs.logger import log_info, log_error
from backup_app.ui.settings_window import SettingsWindow
import os
import sys


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

        self.select_file_button = QPushButton("📂 Выбрать файл")  # 🔥 Новая кнопка
        self.select_file_button.clicked.connect(self.select_file)

        self.backup_button = QPushButton("🚀 Создать бэкап")
        self.backup_button.setEnabled(False)
        self.backup_button.clicked.connect(self.create_backup)

        self.restore_button = QPushButton("🔄 Восстановить")
        self.restore_button.clicked.connect(self.restore_backup)

        self.settings_button = QPushButton("⚙️ Настройки")
        self.settings_button.clicked.connect(self.open_settings)

        self.restore_all_button = QPushButton("🔄 Восстановить всё")  # 🔥 Новая кнопка
        self.restore_all_button.clicked.connect(self.restore_all_files)

        layout = QVBoxLayout()
        layout.addWidget(self.drag_drop_widget)
        layout.addWidget(self.select_file_button)  # 🔥 Новая кнопка выбора файла
        layout.addWidget(self.backup_button)
        layout.addWidget(self.restore_button)
        layout.addWidget(self.restore_all_button)
        layout.addWidget(self.settings_button)
        layout.addWidget(self.log)
        self.central_widget.setLayout(layout)

    def select_file(self):
        """Открывает диалоговое окно для выбора файла"""
        file_dialog = QFileDialog(self)
        file_path, _ = file_dialog.getOpenFileName(self, "Выбрать файл для бэкапа")

        if file_path:
            self.selected_folder = file_path
            self.log.append(f"📂 Выбран файл: {file_path}")
            self.backup_button.setEnabled(True)

    def create_backup(self):
        if self.selected_folder:
            backup_path = create_backup(self.selected_folder)

            if backup_path:
                self.log.append(f"✅ Бэкап создан: {backup_path}")
                self.restore_button.setEnabled(True)
            else:
                self.log.append("❌ Ошибка при создании бэкапа")
        else:
            self.log.append("❌ Ошибка: выберите файл или папку для бэкапа")

    def restore_backup(self):
        """Позволяет выбрать файл и папку для восстановления с обновлённой структурой."""
        file_dialog = QFileDialog(self)
        file_dialog.setDirectory(os.path.abspath("backups/"))
        file_path, _ = file_dialog.getOpenFileName(self, "Выбрать файл для восстановления")

        if not file_path:
            self.log.append("⚠ Выбор отменён, файл не был выбран.")
            return

        file_name = os.path.basename(file_path)
        backup_file = find_latest_backup(file_name)

        if not backup_file:
            self.log.append(f"❌ Ошибка восстановления! Файл {file_name} не найден в backups/")
            return

        restore_path = QFileDialog.getExistingDirectory(self, "Выберите папку для восстановления")

        if not restore_path:
            self.log.append("⚠ Выбор отменён, папка не была выбрана.")
            return

        restored_file = restore_backup(file_name, restore_path)

        if restored_file:
            self.log.append(f"✅ Файл восстановлен в {restore_path}")
            log_info(f"✅ Файл {file_name} восстановлен в {restore_path}")
        else:
            self.log.append(f"❌ Ошибка восстановления! Проверьте содержимое backups/!")
            log_error(f"❌ Ошибка восстановления файла {file_name}")

    def restore_all_files(self):
        """Восстанавливает все файлы из backups/"""
        restore_base_path = os.path.expanduser("~/Downloads/Restore")
        restored_files = restore_all_files(restore_base_path)

        if restored_files:
            self.log.append(f"✅ Все файлы восстановлены в {restore_base_path}")
        else:
            self.log.append("❌ Ошибка восстановления! В папке backups/ нет файлов")

    def open_settings(self):
        self.settings_window = SettingsWindow()
        self.settings_window.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
