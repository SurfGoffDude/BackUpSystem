# 🛠 Backup Manager

**Backup Manager** — это мощное кроссплатформенное приложение для резервного копирования файлов.  
Поддерживает **локальные и удалённые бэкапы**, историю файлов **(как Time Machine)**, **автоматическое расписание** и **загрузку в облачные хранилища (SFTP, FTP, Amazon S3, Google Drive)**.

---

## 🚀 **Функции**
✔ **Простое управление через GUI (PyQt6)**  
✔ **Локальные бэкапы с историей версий**  
✔ **Поддержка удалённых серверов (SFTP/FTP)**  
✔ **Облачные сервисы: Amazon S3, Google Drive**  
✔ **Шифрование файлов перед отправкой (AES-256)**  
✔ **Системные уведомления о завершении бэкапа**  
✔ **Автоматические бэкапы по расписанию**  
✔ **Логирование всех операций**  

---

# 📥 **Установка**

### **1️⃣ Через GitHub (рекомендуемый способ)**
```sh
git clone https://github.com/yourusername/backup_manager.git
cd backup_manager
```

### **2️⃣ Через ZIP-архив**
- Скачай архив с кодом  
- Разархивируй его  
- Перейди в папку через терминал или командную строку:  
```sh
cd /путь/к/распакованной/папке
```

### **3️⃣ Установка зависимостей**
```sh
pip install -r requirements.txt
```

---

# 🖥 **Запуск на macOS, Windows, Linux**

## **🖥 macOS**
```sh
brew install python3
pip3 install -r requirements.txt
python3 backup_app/main.py
```
🔹 **Создание `.app`**
```sh
pyinstaller --onefile --windowed --name "Backup Manager" backup_app/main.py
```

---

## **🖥 Windows**
```sh
pip install -r requirements.txt
python backup_app/main.py
```
🔹 **Создание `.exe`**
```sh
pyinstaller --onefile --windowed --name "Backup Manager" backup_app/main.py
```

---

## **🖥 Linux**
```sh
sudo apt update && sudo apt install python3 python3-pip
pip3 install -r requirements.txt
python3 backup_app/main.py
```
🔹 **Создание `.deb`**
```sh
fpm -s python -t deb setup.py
```

---

# ⚙️ **Настройка сервера (FTP/SFTP)**
1. **В меню "Настройки" выбери "Настройки сервера"**
2. **Введи IP-адрес, логин, пароль, порт (21 - FTP, 22 - SFTP)**
3. **Нажми "Проверить соединение"**
4. **При первом подключении можно автоматически настроить FTP-сервер**  

📌 **Автоматическая настройка FTP** (Ubuntu/Debian):
```sh
sudo apt update
sudo apt install -y vsftpd
sudo systemctl enable vsftpd
echo 'local_enable=YES\nwrite_enable=YES\nchroot_local_user=YES' | sudo tee -a /etc/vsftpd.conf
sudo systemctl restart vsftpd
```

---

# 🔄 **Автоматические бэкапы**
## **macOS (launchd)**
```sh
launchctl load ~/Library/LaunchAgents/com.backup.app.plist
```

## **Linux (cron)**
```sh
crontab -e
```
Добавить строку:
```
0 2 * * * /usr/local/bin/python3 /path/to/backup_app/main.py
```

## **Windows (Task Scheduler)**
```sh
schtasks /create /tn "Backup Task" /tr "python backup_app/main.py" /sc daily /st 02:00
```

---

# 🤝 **Правила разработки (для контрибьюторов)**

## 📌 **Как принять участие в разработке**
1. **Форкни репозиторий** (`Fork` на GitHub)
2. **Склонируй его к себе**  
   ```sh
   git clone https://github.com/yourusername/backup_manager.git
   cd backup_manager
   ```
3. **Создай новую ветку для фичи или исправления**  
   ```sh
   git checkout -b feature/new-feature
   ```
4. **Разработай и протестируй код**
5. **Создай Pull Request (PR) в `main` репозитория**

---

## ✅ **Кодстайл**
- Используем **PEP8**  
- Форматируем код с помощью **`black`**  
- Документируем код **docstrings**  

📌 **Пример функции с документацией:**
```python
def create_backup(source_folder):
    """
    Создаёт резервную копию указанной папки.

    :param source_folder: Путь к папке для бэкапа.
    :return: Путь к созданному архиву.
    """
    pass
```

---

## 🛠 **Структура проекта**
```
BackupApp/
│── backup_app/          
│   ├── main.py          # Главный файл запуска
│   ├── backup/          
│   │   ├── local_backup.py     # Локальное копирование
│   │   ├── remote_backup.py    # Отправка на сервер
│   │   ├── encrypt.py          # Шифрование файлов
│   │   ├── restore.py          # Восстановление данных
│   │   ├── file_integrity.py   # Проверка целостности файлов
│   ├── ui/             
│   │   ├── main_window.py      # Главное окно
│   │   ├── settings_window.py  # Окно настроек
│   │   ├── widgets.py          # Виджеты (Drag & Drop)
│   │   ├── notifications.py    # Системные уведомления
│   │   ├── timeline_window.py  # История файлов (Time Machine)
│   ├── config/          
│   │   ├── settings.py         # Настройки приложения
│   │   ├── scheduler.py        # Планировщик задач
│   ├── services/        
│   │   ├── google_drive.py     # Поддержка Google Drive
│   │   ├── s3_backup.py        # Поддержка Amazon S3
│   │   ├── server_setup.py     # Настройка FTP/SFTP сервера
│   ├── logs/            
│   │   ├── logger.py           # Основной логгер
│   │   ├── backup_logger.py    # Логирование бэкапов
│   │   ├── cloud_logger.py     # Логирование загрузки в облако
│── requirements.txt      # Зависимости
│── setup.py              # Установка пакета
│── README.md             # Документация
```
