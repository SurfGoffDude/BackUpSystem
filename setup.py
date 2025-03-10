from setuptools import setup, find_packages

setup(
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
