from pycpfcnpj import gen, cpfcnpj
#pip install pycpfcnpj ou interpretador: procurar por: pycpfcnpj
#https://github.com/matheuscas/pycpfcnpj

cpfuser = input('digite seu cpf válido: ')

dado = cpfcnpj.validate(cpfuser)

if dado == True:
    print('trueee')
else:
    print('false')

#print(gen.cpf())
#print(gen.cnpj())
#print(gen.cpf_with_punctuation())
#print(gen.cnpj_with_punctuation())


