from fpdf import FPDF, HTMLMixin # pip3 install fpdf
# creating a class inherited from both FPDF and HTMLMixin
class MyFPDF(FPDF, HTMLMixin):
	pass

pdf = FPDF('P', 'mm', 'A4')
pdf.set_font('Arial', '', 12)
#self.image('logo_pb.png', 10, 8, 33) 

# pdf = PDF()
pdf.alias_nb_pages()
pdf.add_page()

for i in range(1, 41):
    pdf.cell(0, 10, 'Printing line number ' + str(i), 0, 1)
pdf.output('tuto2.pdf', 'F')

# pdf = MyFPDF() # instantiating the class
# pdf.add_page() # adding a page

# file = open("file.html", "r") # opening html file 
# Data = file.read() # extracting the data from hte file as a string

# pdf.write_html(data) # HTMLMixin write_html method
#pdf.output('Python_fpdf.pdf', 'F') #saving the file as a pdf