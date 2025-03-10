from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog, QTextEdit, QVBoxLayout, QWidget
from ui.settings_window import SettingsWindow
from backup.local_backup import create_time_machine_backup
from ui.notifications import send_notification
from ui.widgets import DragDropWidget
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Backup Manager")
        self.setGeometry(300, 200, 600, 400)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.log = QTextEdit()
        self.log.setReadOnly(True)

        self.drag_drop_widget = DragDropWidget(self)

        self.backup_button = QPushButton("🚀 Создать бэкап")
        self.backup_button.setEnabled(False)
        self.backup_button.clicked.connect(self.create_backup)

        self.settings_button = QPushButton("⚙️ Настройки")
        self.settings_button.clicked.connect(self.open_settings)

        layout = QVBoxLayout()
        layout.addWidget(self.drag_drop_widget)
        layout.addWidget(self.backup_button)
        layout.addWidget(self.settings_button)
        layout.addWidget(self.log)
        self.central_widget.setLayout(layout)

    def create_backup(self):
        if self.drag_drop_widget.selected_folder:
            backup_path = create_time_machine_backup(self.drag_drop_widget.selected_folder)
            self.log.append(f"✅ Бэкап создан: {backup_path}")
            send_notification("Бэкап завершён", f"Создан: {backup_path}")
        else:
            self.log.append("❌ Ошибка: выберите папку для бэкапа")

    def open_settings(self):
        self.settings_window = SettingsWindow()
        self.settings_window.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
