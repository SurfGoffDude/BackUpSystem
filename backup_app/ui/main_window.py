from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QTextEdit, QVBoxLayout, QWidget
from ui.widgets import DragDropWidget
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

        self.drag_drop_widget = DragDropWidget(self)  # 🔥 Передаём `self` (MainWindow)

        self.backup_button = QPushButton("🚀 Создать бэкап")
        self.backup_button.setEnabled(False)  # ✅ Теперь корректно отключается
        self.backup_button.clicked.connect(self.create_backup)

        layout = QVBoxLayout()
        layout.addWidget(self.drag_drop_widget)
        layout.addWidget(self.backup_button)
        layout.addWidget(self.log)
        self.central_widget.setLayout(layout)

    def create_backup(self):
        if self.selected_folder:
            self.log.append(f"✅ Бэкап создан: {self.selected_folder}")
        else:
            self.log.append("❌ Ошибка: выберите файл или папку для бэкапа")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
