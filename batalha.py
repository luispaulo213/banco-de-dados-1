import sqlite3
import random

# Passo 1: Criar a tabela e inserir os dados do personagem

# Conectar ao banco de dados (isso cria o banco de dados se ele não existir)
conn = sqlite3.connect('ficha_rpg.db')
cursor = conn.cursor()

# Criar a tabela personagem se não existir
cursor.execute('''
CREATE TABLE IF NOT EXISTS personagem (
    id INTEGER PRIMARY KEY,
    nome TEXT,
    classe TEXT,
    raca TEXT,
    nivel INTEGER,
    hp INTEGER,
    forca INTEGER,
    destreza INTEGER,
    inteligencia INTEGER
)
''')

# Inserir os dados do personagem se ele ainda não estiver na tabela
cursor.execute('''
SELECT COUNT(*) FROM personagem WHERE nome = 'Khor'
''')
if cursor.fetchone()[0] == 0:
    cursor.execute('''
    INSERT INTO personagem (nome, classe, raca, nivel, hp, forca, destreza, inteligencia)
    VALUES ('Khor', 'Paladino', 'Goliah', 5, 60, 20, 12, 14)
    ''')

# Commit e fechar a conexão com o banco de dados
conn.commit()

# Passo 2: Iniciar a batalha

# Definindo as variáveis do personagem
nome = 'Khor'
classe = 'Paladino'
raca = 'Goliah'
nivel = 5
hp = 60
forca = 20
destreza = 12
inteligencia = 14
inventario = {"Poção de vida": 10, "Maça Pesada": 1, "Escudo": 1}

# Definindo as variáveis do inimigo
_nome = "Goblin"
_hp = 30
_forca = 10

# Conexão com o banco de dados para pegar os dados do personagem
conn = sqlite3.connect('ficha_rpg.db')
cursor = conn.cursor()

# Consulta para obter os dados do personagem
cursor.execute("SELECT hp, forca FROM personagem WHERE nome = 'Khor'")
dados_personagem = cursor.fetchone()
hp, forca = dados_personagem  # Atualiza o HP e força com os dados do banco de dados

# Fechar a conexão com o banco de dados
conn.close()

# Função para mostrar as opções de ação
def mostrar_opcoes():
    print("\nO que você deseja fazer?")
    print("1. Atacar com Maça Pesada")
    print("2. Usar Poção de Vida")
    print("3. Fugir")

# Função para atacar com a maça (2d6 de dano)
def atacar_com_maca():
    dano_personagem = random.randint(1, 6) + random.randint(1, 6)  # 2d6 de dano
    global _hp
    _hp -= dano_personagem
    print(f"{nome} ataca {_nome} com a Maça Pesada e causa {dano_personagem} de dano!")

# Função para usar poção de vida
def usar_pocao():
    global hp
    if inventario["Poção de vida"] > 0:
        cura = random.randint(10, 20)
        hp += cura
        inventario["Poção de vida"] -= 1
        print(f"{nome} usou uma Poção de Vida e recuperou {cura} HP!")
    else:
        print(f"{nome}, você não tem poções de vida!")

# Função para fugir
def fugir():
    print(f"{nome} tentou fugir, mas não conseguiu escapar!")

# Exibe os dados iniciais
print(f"Dados Iniciais:")
print(f"Nome: {nome} | Classe: {classe} | Raça: {raca}")
print(f"HP: {hp} | Força: {forca}")
print(f"Inimigo: {_nome} | HP: {_hp} | Força: {_forca}")

# Inicia a batalha
turno = 1
while hp > 0 and _hp > 0:
    # Mostra as opções de ação
    mostrar_opcoes()

    # Recebe a escolha do jogador
    acao = input("Escolha uma opção (1, 2 ou 3): ")

    if acao == "1":
        # Jogador escolheu atacar com a maça
        atacar_com_maca()
    elif acao == "2":
        # Jogador escolheu usar poção de vida
        usar_pocao()
    elif acao == "3":
        # Jogador escolheu fugir
        fugir()
    else:
        print("Opção inválida. Tente novamente.")
        continue

    # Inimigo ataca após a escolha do jogador
    if _hp > 0:
        dano_inimigo = random.randint(5, _forca)
        hp -= dano_inimigo
        print(f"{_nome} ataca {nome} e causa {dano_inimigo} de dano!")

    # Exibe o HP atual após a ação
    print(f"{nome} HP: {hp} | {_nome} HP: {_hp}")

# Resultado final da batalha
if hp > 0:
    print(f"\n{nome} venceu a batalha!")
else:
    print(f"\n{_nome} venceu a batalha!")

# Exibe o resultado final dos HPs
print(f"\nResultado Final:")
print(f"{nome} HP: {hp} | {_nome} HP: {_hp}")