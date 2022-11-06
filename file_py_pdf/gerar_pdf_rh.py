from fpdf import FPDF # pip3 install fpdf
import csv

class PDF(FPDF):
    def header(self):
        
        #self.image('logo_pb.png', 10, 8, 33) # configurar uma logo
        self.set_font('Arial', 'B', 15) # Arial bold 15
        
        self.cell(80) # Move to the right
        
        self.cell(30, 10, 'Times NBA', 0, 0, 'C') # Title cabeçalho - centralizado
        
        self.ln(20) # Line break

    # Page footer
    def footer(self):
        
        self.set_y(-15) # Position at 1.5 cm from bottom
        
        self.set_font('Arial', 'I', 8) # Arial italic 8
        
        self.cell(0, 10, 'Página ' + str(self.page_no()) + '/{nb}', 0, 0, 'C') # Page number

# Instantiation of inherited class
pdf = PDF()
pdf.alias_nb_pages()
pdf.add_page()
pdf.set_font('Times', '', 12)

with open('times_nba.csv', 'r') as arquivo:
    arquivo_csv = csv.reader(arquivo, delimiter=":")

    for i, linha in enumerate(arquivo_csv):
        pdf.cell(0, 10, "lista: Time {} ano {}".format(linha[0], linha[1]) , 0, 1)
        pdf.add_page() # caso queria colocar cada informação em uma pagina
pdf.output('tuto2.pdf', 'F')