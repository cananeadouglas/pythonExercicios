from openpyxl import Workbook
import datetime
import openpyxl

#Globais
book_k = openpyxl.Workbook()
name_aba = "Sheet"
nome_aba = book_k.active #Aba ativa

name_file = input("""
                Digite o nome do arquivo que deseja salvar,
                não esqueça do .xlsx no final
                
                """)

# Criar uma planilha(book)
def create_planilha(name_file):
    opcao = input("""
        quer definir nome da aba? 
        digite S para SIM,
        e N para NÃO definir
        e C para Incrementar uma nova aba padrão 
        """).lower()

    if opcao == "s":
        create_sheets(name_file)
    elif opcao == "n":
        book_k.save(name_file)
    elif opcao == "c":
        book_k.create_sheet()
        book_k.save(name_file)
    return

# Criar abas
def create_sheets(name_file):
    nome_sheets = input("qual vai ser o nome da aba? ")
    if nome_sheets == "":
        # Variável vazia
        book_k.create_sheet()
        print("""   #Criado nome padrão#    """)
        book_k.save(name_file)
    else: 
        book_k.create_sheet(nome_sheets)
        book_k.save(name_file)
    return

# Usar aba
def use_sheet(name_file, book_k):
    print("""  """, book_k.sheetnames)
    select_aba = input("""
            Digite o nome da aba
            que deseja usar, conforme esta escrito
            
            """)
    name_aba = book_k[select_aba]
    #book_k = openpyxl.load_workbook(name_file)
    save(name_file)
    
    return name_aba

# Inserindo dados
def insert(name_aba):
    
    name_aba.append(["Frutas", "Quantidade", "Preço"])
    name_aba.append(["bandeja 20", "2", "R$ 20,00"])

    print("Inserindo dados em: ", name_aba)
    colunas = int(input("quantas colunas deseja inserir? "))

    for linha in colunas:
        linha = input("digite alguma coisa")
        name_aba.append(linha)
    return

# Leitura de dados
def read(nome_aba):
    for rows in nome_aba.iter_rows(min_row=2):
        print(f'{rows[0].value}, {rows[1].value}, {rows[2].value}')

    return

# Salvar alterações
def save(name_file):
    book_k.save(name_file)
    return

cont = 0

while cont == 0:
    texto = int(input("""
        Digite 1 para criar planilha
        Digite 2 para criar abas
        Digite 3 para mostrar nome das abas
        Digite 4 para inserir dados
        Digite 5 para seleção de abas
        Digite 6 para mostrar dados
        Digite 0 para sair

        informações a serem consideradas:
        -> {} <- nome do arquivo
        -> {} <- nome da aba
        """.format(name_file, name_aba)))
    if texto == cont:
        # Saída do programa
        cont = 1
        break
    elif texto == 1:
        create_planilha(name_file)
        print("sucesso")

    elif texto == 2:
        create_sheets(name_file)

    elif texto == 3:
        print(" ")
        print("""  """, book_k.sheetnames)
        
    elif texto == 4:
        insert(nome_aba)
        print("Sucesso")
    
    elif texto == 5:
        use_sheet(name_file, book_k)
        print("Sucesso")
    
    elif texto == 6:
        read(nome_aba)


    else:
        print("sem resposta")



