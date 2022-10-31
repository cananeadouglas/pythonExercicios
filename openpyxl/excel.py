import openpyxl

#Criar uma planilha(book)
#book = openpyxl.Workbook()

#Visualizar abas existentes
#print(book.sheetnames)

#Criar abas
#book.create_sheet('Doces')

#Selecionar uma aba para adicionar dados.
#doces_page = book['Doces']

#inserindo dados
#doces_page.append(["Frutas", "Quantidade", "Preço"])
#doces_page.append(["bandeja 20", "2", "R$ 20,00"])
#doces_page.append(["Frango", "5", "R$ 30,00"])
#doces_page.append(["Carne de Porco", "9", "R$ 45,00"])

#salvar a planilha com os dados
#https://pt.myservername.com/hands-python-openpyxl-tutorial-with-examples
#book.save('primeira_plan.xlsx')

#ler e inserir dados em uma planilha já existente
# abrir um arquivo
book = openpyxl.load_workbook('primeira_plan.xlsx')

# selecionar a aba
frutas_page = book['Doces']

#imprimindo os dados de cada linha
for rows in frutas_page.iter_rows(min_row=2):
    for cell in rows:
        print(cell.value)

for rows in frutas_page.iter_rows(min_row=2):
    print(rows[0].value,"|", rows[1].value,"|", rows[2].value)

for rows in frutas_page.iter_rows(min_row=2):
    print(f'{rows[0].value}, {rows[1].value}, {rows[2].value}')

#coluna 0
for rows in frutas_page.iter_rows(min_row=2):
    print(f'{rows[0].value}')

#alteração de dados

for rows in frutas_page.iter_rows(min_row=2):
    for cell in rows:
        if cell.value == 'uuu':
            cell.value = 'Frutas 1'

book.save('primeira_plan.xlsx')