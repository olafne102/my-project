import sqlite3
import pandas as pd
from datetime import datetime

# Kết nối file database
conn = sqlite3.connect("history.db", check_same_thread=False)
cursor = conn.cursor()

# 👉 Luôn drop bảng cũ (nếu có) rồi tạo lại bảng mới
cursor.execute("DROP TABLE IF EXISTS history")

cursor.execute("""
CREATE TABLE history (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    text TEXT,
    sentiment TEXT,
    time TEXT
)
""")
conn.commit()


def save_history(text, senti):
    cursor.execute(
        "INSERT INTO history(text, sentiment, time) VALUES (?, ?, ?)",
        (text, senti, datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    )
    conn.commit()


def get_history():
    return cursor.execute("SELECT * FROM history ORDER BY id DESC").fetchall()


def clear_history():
    cursor.execute("DELETE FROM history")
    conn.commit()


def load_file(file):
    if file.name.endswith(".csv"):
        return pd.read_csv(file)
    if file.name.endswith(".xlsx"):
        return pd.read_excel(file)
    return None
