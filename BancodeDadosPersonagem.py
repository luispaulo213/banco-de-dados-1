import sqlite3

# Conectando ao banco de dados (se o banco não existir, ele será criado)
conexao = sqlite3.connect('ficha_rpg.db')

# Criando um cursor para executar comandos SQL
cursor = conexao.cursor()

# Criando a tabela para armazenar as informações da ficha, caso ainda não exista
cursor.execute('''
    CREATE TABLE IF NOT EXISTS ficha_rpg (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        classe TEXT,
        raca TEXT,
        nivel INTEGER,
        hp INTEGER,
        forca INTEGER,
        destreza INTEGER,
        inteligencia INTEGER,
        inventario TEXT
    )
''')

# Confirmando as alterações
conexao.commit()

# Inserindo dados do personagem "Khor"
cursor.execute('''
    INSERT INTO ficha_rpg (nome, classe, raca, nivel, hp, forca, destreza, inteligencia, inventario)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
''', ("Khor", "Paladino", "Goliah", 5, 60, 20, 12, 14, "Maça Pesada, Escudo, Poção de vida(x10)"))

# Confirmando as alterações
conexao.commit()

# Consultando os dados inseridos
cursor.execute("SELECT * FROM ficha_rpg WHERE nome = 'Khor'")
resultado = cursor.fetchone()

# Exibindo os dados de Khor
print(f"ID: {resultado[0]}, Nome: {resultado[1]}, Classe: {resultado[2]}, Raça: {resultado[3]}, Nível: {resultado[4]}, HP: {resultado[5]}, Força: {resultado[6]}, Destreza: {resultado[7]}, Inteligência: {resultado[8]}, Inventário: {resultado[9]}")

# Fechando a conexão com o banco de dados
conexao.close()
