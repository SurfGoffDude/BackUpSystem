from PyQt6.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QComboBox
from config.settings import save_settings, load_settings
from services.server_setup import configure_ftp_server
import paramiko
import ftplib

class ServerSettingsWindow(QDialog):
    """Окно настроек удалённого сервера"""
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Настройки удалённого сервера")
        self.setGeometry(400, 250, 400, 300)

        self.label = QLabel("Введите данные для подключения:")
        self.server_ip = QLineEdit()
        self.server_ip.setPlaceholderText("IP-адрес сервера")
        self.username = QLineEdit()
        self.username.setPlaceholderText("Логин")
        self.password = QLineEdit()
        self.password.setPlaceholderText("Пароль")
        self.password.setEchoMode(QLineEdit.EchoMode.Password)
        self.port = QLineEdit()
        self.port.setPlaceholderText("Порт (по умолчанию 21 для FTP, 22 для SFTP)")
        self.server_type = QComboBox()
        self.server_type.addItems(["SFTP", "FTP"])

        self.save_button = QPushButton("💾 Сохранить")
        self.save_button.clicked.connect(self.save_server_settings)

        self.test_button = QPushButton("🔄 Проверить соединение")
        self.test_button.clicked.connect(self.test_connection)

        self.setup_button = QPushButton("⚙️ Настроить сервер (FTP)")
        self.setup_button.clicked.connect(self.setup_ftp_server)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.server_ip)
        layout.addWidget(self.username)
        layout.addWidget(self.password)
        layout.addWidget(self.port)
        layout.addWidget(self.server_type)
        layout.addWidget(self.save_button)
        layout.addWidget(self.test_button)
        layout.addWidget(self.setup_button)
        self.setLayout(layout)

    def save_server_settings(self):
        """Сохраняет данные сервера"""
        settings = load_settings()
        settings["server"] = {
            "ip": self.server_ip.text(),
            "username": self.username.text(),
            "password": self.password.text(),
            "port": int(self.port.text()) if self.port.text() else 21,
            "type": self.server_type.currentText()
        }
        save_settings(settings)
        self.close()

    def test_connection(self):
        """Проверяет соединение с сервером"""
        settings = load_settings().get("server", {})
        if settings["type"] == "SFTP":
            try:
                client = paramiko.Transport((settings["ip"], settings["port"]))
                client.connect(username=settings["username"], password=settings["password"])
                client.close()
                print("✅ SFTP-соединение успешно установлено")
            except Exception as e:
                print(f"❌ Ошибка подключения: {e}")

        else:
            try:
                ftp = ftplib.FTP()
                ftp.connect(settings["ip"], settings["port"])
                ftp.login(settings["username"], settings["password"])
                ftp.quit()
                print("✅ FTP-соединение успешно установлено")
            except Exception as e:
                print(f"❌ Ошибка подключения: {e}")

    def setup_ftp_server(self):
        """Настраивает FTP-сервер на удалённом сервере"""
        settings = load_settings().get("server", {})
        configure_ftp_server(settings["ip"], settings["username"], settings["password"])
