import pandas as pd

# Dados das tabelas como dicionários
racas_data = {
    "Raças": ["TIELFING", "ANÃO", "ELFO", "HALFLING", "HUMANO", "DRRACONATO", "GNOMO", "MEIO-ELFO", "MEIO-ORC", "TABAXI", "TRITÃO", "AARACROKA"],
    "força": [1, 2, 0, 0, 1, 2, 0, 0, 2, 0, 0, 0],
    "destreza": [0, 0, 2, 2, 1, 0, 0, 0, 0, 2, 0, 2],
    "constituição": [0, 2, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0],
    "inteligência": [0, 0, 0, 0, 1, 0, 2, 0, 0, 0, 0, 1],
    "sabedoria": [0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0],
    "carisma": [2, 0, 0, 0, 1, 0, 0, 2, 0, 0, 0, 0],
}

classes_data = {
    "Classe": ["ARTIFICE(ATF)", "BARBARO(BARB)", "BARDO(BARD)", "BRUXO(BRUX)", "CLÉRIGO(CLÉR)", "DRUÍDA(DRUI)",
               "FEITIÇEIRO(FEIT)", "PATRULHEIRO(PAT)", "GUERREIRO(GUERR)", "LADINO(LAD)", "MAGO(MAG)", "MONGE(MONG)", "PALADINO(PLD)"],
    "força": [0, 2, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 1],
    "destreza": [0, 0, 1, 0, 0, 0, 0, 2, 0, 2, 0, 2, 0],
    "constituição": [0, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
    "inteligência": [2, 0, 0, 1, 0, 0, 1, 0, 0, 0, 2, 0, 0],
    "sabedoria": [0, 0, 0, 0, 2, 2, 0, 1, 0, 0, 0, 1, 0],
    "carisma": [0, 0, 2, 2, 0, 0, 2, 0, 0, 0, 0, 0, 2],
}

subclasses_data = {
    "Subclasse": ["FERREIRO DE BATALHA(ATF)", "ARMEIRO(ATF)", "ALQUIMISTA(ATF)", "BERSEKER(BARB)", "TOTEMISTA(BARB)",
                  "FEITICEIRO DA ALMA(BARD)", "PATRONO DAS FADAS(BRUX)", "PATRONO DOS INFERNOS(BRUX)", "PATRONO DO ABISMO(BRUX)",
                  "DOMÍNIO DA VIDA (CLÉR)", "DOMINIO DA GUERRA(CLÉR)", "DOMÍNIO DO CONHECIMENTO(CLÉR)", "GUARDIÃO(DRUI)",
                  "FEITIÇEIRO DRACONICO(FEIT)", "MAGIA SELVAGEM(FEIT)", "CAÇADOR(PAT)", "CAMPEÃO(GUERR)",
                  "CAVALEIRO ARCÂNICO(GUERR)", "ASSASSINO(LAD)", "TRAPACEIRO ARCÂNO(LAD)", "NECROMANTE(MAG)", "CONJURADOR(MAG)",
                  "CAMINHO DA MÃO ABERTA(MONG)", "CAMINHO DA SOMBRA(MONG)", "CAMINHO DOS QUATRO ELEMENTOS(MONG)",
                  "KENSAY(MONG)", "JURADO DA VINGANÇA(PLD)", "JURADO DA DEVOÇÃO(PLD)", "JURADO DOS ANCIÕES(PLD)"],
    "força": [2, 1, 0, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1, 2, 0],
    "destreza": [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 2, 1, 0, 0, 2, 2, 2, 1, 1, 0, 0],
    "constituição": [1, 1, 0, 2, 2, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, -2, 0, 0, 0, 1, 0, 0, 1, 2],
    "inteligência": [0, 2, 2, 0, 0, 0, 1, 1, 2, 0, 0, 2, 0, 0, 2, 0, 0, 2, 0, 1, 3, 2, 0, 0, 0, 0, 0, 0, 0],
    "sabedoria": [0, 0, 1, -1, 1, 1, 0, 0, 0, 2, 1, 1, 2, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 2],
    "carisma": [0, 0, 0, 0, 0, 2, 1, 2, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1, 0],
}

# Criar DataFrames
df_racas = pd.DataFrame(racas_data)
df_classes = pd.DataFrame(classes_data)
df_subclasses = pd.DataFrame(subclasses_data)

# Padronizar colunas
df_racas.columns = df_racas.columns.str.strip().str.lower()
df_classes.columns = df_classes.columns.str.strip().str.lower()
df_subclasses.columns = df_subclasses.columns.str.strip().str.lower()

# Entrada do usuário
raca_escolhida = "MEIO-ORC"
classe_escolhida = "MONGE(MONG)"
subclasse_escolhida = "KENSAY(MONG)"

# Localizar as linhas correspondentes
raca = df_racas[df_racas["raças"] == raca_escolhida].iloc[0]
classe = df_classes[df_classes["classe"] == classe_escolhida].iloc[0]
subclasse = df_subclasses[df_subclasses["subclasse"] == subclasse_escolhida].iloc[0]

# Somar os valores das tabelas, lidando com NaN
atributos_finais = (raca[1:].fillna(0) + classe[1:].fillna(0) + subclasse[1:].fillna(0)).astype(int)

# Exibir os atributos finais
print("Atributos finais:")
print(atributos_finais)
