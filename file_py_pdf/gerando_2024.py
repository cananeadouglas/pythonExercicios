# pip3 install reportlab

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

from datetime import datetime

# transformar
def mm_to_p(mm):
    return mm / 0.352777

atual = datetime.now()
#print(atual)

nome = 'Douglas'
telefone = 82999010101
ordem = '0001'
nomeCliente = 'Chiquinha'
obs = 'notebook sem dar tela, precisando de manutenção'

descricao = ['Descrição', 'Valor Und.', 'Quantidade', 'Total']

pdf = canvas.Canvas('/home/jdfc1/cananeadouglas_git/pythonExercicios/file_py_pdf/exemplo.pdf', pagesize=A4)


# pdf.drawString(285, 800, 'Olá Primo!')
# A4 210 x 297 mm

#Hora
pdf.setFont('Helvetica', 10)
pdf.drawString(mm_to_p(15), mm_to_p(281), atual.strftime('%Y-%m-%d, %H:%M:%S'))

#Nome
pdf.drawString(mm_to_p(160), mm_to_p(270), f'Feito por: {nome}')

#Telefone
pdf.drawString(mm_to_p(160), mm_to_p(265), f'Fone: {telefone}')

#Orçamento
pdf.setFont('Helvetica-Bold', 40)
pdf.drawString(mm_to_p(15), mm_to_p(265), 'Orçamento')

#ordem
pdf.setFont('Helvetica-Bold', 25)
pdf.drawString(mm_to_p(15), mm_to_p(254), f'de serviço tecnológico n° {ordem}')

#cliente observações
pdf.setFont('Helvetica', 11)
pdf.drawString(mm_to_p(15), mm_to_p(234), f'Solicitado por {nomeCliente}. Observações: {obs}')

#linha ( xi y xf y )
pdf.line(mm_to_p(15), mm_to_p(245), mm_to_p(192), mm_to_p(245))

eixoX = 15

for desc in descricao:
    pdf.setFont('Helvetica-Bold', 14)
    pdf.drawString(mm_to_p(eixoX), mm_to_p(220), f'{desc}')
    eixoX += 50


with open('/home/jdfc1/cananeadouglas_git/pythonExercicios/file_py_pdf/gerando_2024.csv', 'r', encoding='utf-8') as arquivo:
    arquivo_csv = arquivo.readlines()

    #resetando as po
    eixoY = 210
    eixoX = 15

    for linha in arquivo_csv:
        descr, unitario, quant = linha.strip().split(':')
        pdf.setFont('Helvetica', 9)

        dado1 = float(unitario)
        dado2 = int(quant)
        dado3 = dado1 * dado2
        dado4 = dado3 + dado3

        pdf.drawString(mm_to_p(eixoX), mm_to_p(eixoY), descr)
        eixoX += 50
        pdf.drawString(mm_to_p(eixoX), mm_to_p(eixoY), f'R$ {unitario}')
        eixoX += 50
        pdf.drawString(mm_to_p(eixoX), mm_to_p(eixoY), f'{quant} und.')
        eixoX += 50
        pdf.drawString(mm_to_p(eixoX), mm_to_p(eixoY), f'R$ {str(round(dado3,2))}')
        eixoX += 50

        eixoY = eixoY - 8
        eixoX = 15

        #eixoY -= 8

    pdf.setFont('Helvetica-Bold', 11)
    pdf.drawString(mm_to_p(150), mm_to_p(160), f'Total: R$ {dado4}')

pdf.save()