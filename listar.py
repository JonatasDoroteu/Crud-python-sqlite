import sqlite3

conn = sqlite3.connect('meu_banco.db')
cursor = conn.cursor()

cursor.execute("SELECT * FROM usuarios")

usuarios = cursor.fetchall()

print("\n=== Lista de usuários ===")

for usuario in usuarios:
    print(f"""
ID: {usuario[0]}
Nome: {usuario[1]}
Email: {usuario[2]}

""")
    cursor.execute("DELETE FROM usuarios WHERE id = 4")

conn.commit()

conn.close()