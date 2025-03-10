import platform

if platform.system() == "Darwin":
    from pync import Notifier
elif platform.system() == "Windows":
    from plyer import notification

def send_notification(title, message):
    """Отправляет системное уведомление"""
    if platform.system() == "Darwin":
        Notifier.notify(message, title=title)
    elif platform.system() == "Windows":
        notification.notify(title=title, message=message, app_name="Backup Manager")
    else:
        print(f"🔔 {title}: {message}")
