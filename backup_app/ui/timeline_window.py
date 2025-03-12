from PyQt6.QtWidgets import QDialog, QVBoxLayout, QLabel, QListWidget, QPushButton
from PyQt6.QtChart import QChart, QChartView, QLineSeries
from PyQt6.QtCore import Qt, QPointF
import os
from datetime import datetime
from backup_app.backup.restore import restore_backup

BACKUP_DIR = os.path.expanduser("~/Downloads/backups/")


class TimelineWindow(QDialog):
    """Окно с таймлайном истории файлов."""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("История файлов")
        self.setGeometry(400, 250, 600, 400)

        self.label = QLabel("Выберите файл:")
        self.file_list = QListWidget()
        self.load_files()

        self.chart_view = QChartView()
        self.chart = QChart()
        self.chart.setTitle("Версии файла")
        self.chart_view.setChart(self.chart)

        self.restore_button = QPushButton("🔄 Восстановить выбранную версию")
        self.restore_button.setEnabled(False)
        self.restore_button.clicked.connect(self.restore_version)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.file_list)
        layout.addWidget(self.chart_view)
        layout.addWidget(self.restore_button)
        self.setLayout(layout)

        self.file_list.itemClicked.connect(self.update_chart)

    def load_files(self):
        """Загружает список файлов из бэкапов."""
        file_versions = {}
        for backup in sorted(os.listdir(BACKUP_DIR)):
            backup_path = os.path.join(BACKUP_DIR, backup)
            if os.path.isdir(backup_path):
                for root, _, files in os.walk(backup_path):
                    for file in files:
                        if file not in file_versions:
                            file_versions[file] = []
                        file_versions[file].append(backup)

        for file in file_versions.keys():
            self.file_list.addItem(file)

        self.file_versions = file_versions

    def update_chart(self, item):
        """Обновляет таймлайн файла."""
        self.chart.removeAllSeries()
        file_name = item.text()
        versions = self.file_versions.get(file_name, [])

        series = QLineSeries()
        for i, version in enumerate(versions):
            timestamp = datetime.strptime(version, "%Y-%m-%d_%H-%M-%S").timestamp()
            series.append(QPointF(timestamp, i))

        self.chart.addSeries(series)
        self.chart.createDefaultAxes()
        self.restore_button.setEnabled(True)

    def restore_version(self):
        """Восстанавливает выбранную версию файла."""
        selected_file = self.file_list.currentItem().text()
        selected_version = self.file_versions[selected_file][-1]  # Последняя версия

        restore_file(selected_file, selected_version, "/Users/username/Desktop")
        self.close()
