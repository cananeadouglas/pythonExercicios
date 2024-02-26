import csv

with open('/home/jdfc1/cananeadouglas_git/pythonExercicios/file_py_pdf/times_nba.csv', 'r') as arquivo:
    arquivo_csv = csv.reader(arquivo, delimiter=":")

    for i, linha in enumerate(arquivo_csv):
                        

            print(f"Time {linha[0]} ano {linha[1]}")