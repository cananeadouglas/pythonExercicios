import formato_preco

def aumento(valor, porcentagem, formato=False):
    r = valor + (valor * (porcentagem / 100))
    if formato:
        return formato_preco.real(r)
    else:
        return r

def desconto(valor, porcentagem, formato=False):
    r = valor - (valor * (porcentagem / 100))
    
    if formato:
        return formato_preco.real(r)
    else:
        return r

