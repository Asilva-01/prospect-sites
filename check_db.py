import sqlite3

conn = sqlite3.connect('prospector.db')
cursor = conn.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()
print("Tabelas:", tables)

for t in tables:
    t_name = t[0]
    cursor.execute(f"PRAGMA table_info({t_name});")
    print(f"\n--- Schema {t_name} ---")
    cols = [col[1] for col in cursor.fetchall()]
    print(cols)
    cursor.execute(f"SELECT * FROM {t_name}")
    rows = cursor.fetchall()
    print(f"Total rows in {t_name}: {len(rows)}")
    for r in rows:
        print(r)

conn.close()
