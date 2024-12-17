import pandas as pd

# Carregar o arquivo e obter os nomes das planilhas
tcc = 'Troçosfinalizados.xlsx'
xls = pd.ExcelFile(tcc).sheet_names
print(xls)  # Mostra as planilhas disponíveis

# Lendo as planilhas
sheets = []
for sheetname in xls:
    sheet = pd.read_excel(tcc, sheet_name=sheetname)
    sheets.append(sheet)

# Função para converter o nome da célula (ex: "B2") para índices
def convertcelforind(cel):
    column = ord(cel[0].upper()) - ord('A')  # Converte a letra para o índice da coluna
    line = int(cel[1:]) - 1  # Converte a linha para índice (0-base)
    return column, line

# Pedir para o usuário inserir as células
selectedvalues = []
for i, sheet in enumerate(sheets):
    celula = input(f'Digite uma célula para a tabela "{xls[i]}" (exemplo B2, C4, etc.): ')
    column, line = convertcelforind(celula)
    valor = sheet.iloc[line, column]  # Acessa o valor na célula
    print(f'O valor na célula {celula} é: {valor}')
    selectedvalues.append(valor)
