import paramiko


def configure_ftp_server(server_ip, username, password):
    """Настраивает FTP-сервер на удалённом сервере"""
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(server_ip, username=username, password=password)

        commands = [
            "sudo apt update",
            "sudo apt install -y vsftpd",
            "sudo systemctl enable vsftpd",
            "echo 'local_enable=YES\nwrite_enable=YES\nchroot_local_user=YES' | sudo tee -a /etc/vsftpd.conf",
            "sudo systemctl restart vsftpd"
        ]

        for cmd in commands:
            stdin, stdout, stderr = ssh.exec_command(cmd)
            print(stdout.read().decode(), stderr.read().decode())

        ssh.close()
        print("✅ FTP-сервер настроен!")
    except Exception as e:
        print(f"❌ Ошибка настройки сервера: {e}")
