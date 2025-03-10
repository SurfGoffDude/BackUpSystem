import hashlib

def calculate_hash(file_path):
    """Вычисляет SHA-256 хеш файла."""
    hasher = hashlib.sha256()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hasher.update(chunk)
    return hasher.hexdigest()

def verify_file_integrity(original_file, uploaded_file):
    """Сравнивает хеши файлов для проверки целостности."""
    original_hash = calculate_hash(original_file)
    uploaded_hash = calculate_hash(uploaded_file)

    if original_hash == uploaded_hash:
        return True
    return False
