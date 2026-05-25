import sqlite3

conn = sqlite3.connect('meu_banco.db')
cursor = conn.cursor()

nome = input("Nome: ")
email = input("Email: ")

cursor.execute("""
INSERT INTO usuarios (nome, email)
VALUES (?, ?)
""", (nome, email))

conn.commit()
conn.close()

print("Usuário cadastrado!")