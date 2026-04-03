import sqlite3
from pathlib import Path

def test_requirements_file_exists():
    assert Path("requirements.txt").exists()

def test_app_file_exists():
    assert Path("app.py").exists()

def test_database_connection():
    conn = sqlite3.connect("test_test.db")
    assert conn is not None
