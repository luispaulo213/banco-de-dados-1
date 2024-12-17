import pandas as pd

tcc = 'Troçosfinalizados.xlsx'
sheetname = pd.ExcelFile(tcc).sheet_names

racas = pd.read_excel(tcc, sheet_name=sheetname[0])
classes = pd.read_excel(tcc, sheet_name=sheetname[1])
subclasses = pd.read_excel(tcc, sheet_name=sheetname[2])
print(racas)
print(classes)
print(subclasses)