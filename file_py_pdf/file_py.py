import csv

with open('times_nba.csv', 'r') as arquivo:
    arquivo_csv = csv.reader(arquivo, delimiter=":")

    for i, linha in enumerate(arquivo_csv):
                        

            print("lista: Time {} ano {}".format(linha[0], linha[1]))