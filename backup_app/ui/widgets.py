from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel
from PyQt6.QtCore import Qt

class DragDropWidget(QWidget):
    """Виджет для Drag & Drop файлов и папок"""
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAcceptDrops(True)
        self.label = QLabel("Перетащите файлы сюда", self)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        self.setLayout(layout)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dropEvent(self, event):
        files = [url.toLocalFile() for url in event.mimeData().urls()]
        if files:
            self.parent().selected_folder = files[0]
            self.label.setText(f"Выбрано: {files[0]}")
            self.parent().backup_button.setEnabled(True)  # 🔥 Теперь кнопка активируется!

