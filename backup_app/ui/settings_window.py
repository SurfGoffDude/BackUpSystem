from PyQt6.QtWidgets import QDialog, QVBoxLayout, QLabel, QPushButton, QCheckBox, QLineEdit, QFileDialog


class SettingsWindow(QDialog):
    """Окно настроек приложения"""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Настройки")
        self.setGeometry(400, 250, 400, 300)

        self.label = QLabel("🔧 Настройки резервного копирования")

        self.auto_backup_checkbox = QCheckBox("Автоматический бэкап по расписанию")

        self.backup_folder_button = QPushButton("📁 Выбрать папку для бэкапов")
        self.backup_folder_button.clicked.connect(self.select_backup_folder)
        self.backup_folder_label = QLabel("Не выбрано")

        self.save_button = QPushButton("💾 Сохранить настройки")

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.auto_backup_checkbox)
        layout.addWidget(self.backup_folder_button)
        layout.addWidget(self.backup_folder_label)
        layout.addWidget(self.save_button)
        self.setLayout(layout)

    def select_backup_folder(self):
        folder = QFileDialog.getExistingDirectory(self, "Выбрать папку")
        if folder:
            self.backup_folder_label.setText(f"📂 {folder}")


