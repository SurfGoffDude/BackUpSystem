import json
import os

CONFIG_FILE = "config/settings.json"

DEFAULT_SETTINGS = {
    "backup_folder": "backups/",
    "auto_backup": False,
    "backup_interval": 24,
    "server": {
        "ip": "",
        "username": "",
        "password": "",
        "port": 21,
        "type": "FTP"
    },
    "encryption": {
        "enabled": False
    }
}

def load_settings():
    """Загружает настройки из JSON-файла."""
    if not os.path.exists(CONFIG_FILE):
        save_settings(DEFAULT_SETTINGS)
    with open(CONFIG_FILE, "r", encoding="utf-8") as file:
        return json.load(file)

def save_settings(settings):
    """Сохраняет настройки в JSON-файл."""
    with open(CONFIG_FILE, "w", encoding="utf-8") as file:
        json.dump(settings, file, indent=4)

def update_setting(key, value):
    """Обновляет отдельную настройку."""
    settings = load_settings()
    keys = key.split(".")
    
    data = settings
    for k in keys[:-1]:
        data = data.get(k, {})

    data[keys[-1]] = value
    save_settings(settings)
