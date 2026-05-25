import sqlite3

conn = sqlite3.connect('meu_banco.db')
cursor = conn.cursor()

# Deletar todos os usuários
cursor.execute("DELETE FROM usuarios")

# Salvar alterações
conn.commit()

print("Todos os usuários foram deletados!")

# Fechar conexão
conn.close()