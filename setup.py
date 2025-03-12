# from setuptools import setup, find_packages

'''import sys
from cx_Freeze import setup, Executable

executables = [Executable("backup_app/main.py", target_name="Backup Manager")]

options = {
    "build_exe": {
        "packages": ["PyQt6", "os"],
        "include_files": ["backup_app/"]
    }
}

setup(
    name="Backup Manager",
    version="1.0",
    description="Backup system",
    options=options,  # ✅ Передаём `options`, а не `dict`
    executables=executables
)'''

'''setup(
    name="backup_manager",
    version="1.0.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="Простое GUI-приложение для резервного копирования",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/backup_manager",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "PyQt6",
        "paramiko",
        "boto3",
        "cryptography",
        "google-auth",
        "google-auth-oauthlib",
        "google-auth-httplib2",
        "googleapiclient",
        "plyer",
        "pync"
    ],
    entry_points={
        "console_scripts": [
            "backup-manager = backup_app.main:setup_app",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: MacOS",
    ],
)
'''

from setuptools import setup

APP = ['backup_app/main.py']
DATA_FILES = []
OPTIONS = {
    'argv_emulation': True,
    'packages': ['PyQt6'],
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
