import streamlit as st
import pandas as pd
from datetime import datetime
import sqlite3

conn = sqlite3.connect("server.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE,
    password TEXT,
    role TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS products(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_name TEXT,
    category TEXT,
    quantity INTEGER,
    price REAL,
    supplier TEXT,
    date_added TEXT               
)
""")

conn.commit()