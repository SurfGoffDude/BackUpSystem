import os
import platform
import subprocess
from config.settings import load_settings


def schedule_backup():
    """Запускает бэкап по расписанию в зависимости от ОС."""
    settings = load_settings()
    interval = settings["backup_interval"] * 3600
    script_path = os.path.abspath("backup/local_backup.py")

    if platform.system() == "Darwin":
        setup_launchd(interval, script_path)
    elif platform.system() == "Linux":
        setup_cron(interval, script_path)
    elif platform.system() == "Windows":
        setup_task_scheduler(interval, script_path)
    else:
        print("Операционная система не поддерживается.")


def setup_launchd(interval, script_path):
    """Настраивает запуск через launchd (macOS)."""
    plist_path = os.path.expanduser("~/Library/LaunchAgents/com.backup.app.plist")

    plist_content = f"""<?xml version="1.0" encoding="UTF-8"?>
    <plist version="1.0">
        <dict>
            <key>Label</key>
            <string>com.backup.app</string>
            <key>ProgramArguments</key>
            <array>
                <string>/usr/local/bin/python3</string>
                <string>{script_path}</string>
            </array>
            <key>StartInterval</key>
            <integer>{interval}</integer>
            <key>RunAtLoad</key>
            <true/>
        </dict>
    </plist>
    """

    with open(plist_path, "w") as file:
        file.write(plist_content)

    subprocess.run(["launchctl", "load", plist_path])
    print(f"Бэкап запланирован каждые {interval // 3600} часов (macOS).")


def setup_cron(interval, script_path):
    """Настраивает cron-задачу для Linux."""
    cron_command = f"python3 {script_path}"
    cron_entry = f"0 */{interval // 3600} * * * {cron_command}"

    subprocess.run("(crontab -l; echo '{}') | crontab -".format(cron_entry), shell=True)
    print(f"Бэкап запланирован каждые {interval // 3600} часов (Linux).")


def setup_task_scheduler(interval, script_path):
    """Настраивает Windows Task Scheduler."""
    task_name = "BackupTask"
    command = f'schtasks /create /tn "{task_name}" /tr "python {script_path}" /sc HOURLY /mo {interval // 3600} /f'

    subprocess.run(command, shell=True)
    print(f"Бэкап запланирован каждые {interval // 3600} часов (Windows).")


if __name__ == "__main__":
    schedule_backup()
