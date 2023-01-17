class Evento:
    #construtores
    def __init__(self, nome="oi"):
        #self.nome_do_atributo
        self.nome = nome
        self.local = "Brasil"
        
    def altera_nome_evento(self, novo_nome):
        print("Alterando nome evento")
        self.nome = novo_nome
    
    def metodo_instancia(self):
        return ("metodo de instância chamado", self)

    @classmethod
    def metodo_classe(cls):
        return ("método de classe chamado", cls)
    
    @staticmethod
    def metodo_estatico():
        return "Estático Chamado"

# obj.metodo(1,2,3) => evento.metodo(obj. 1,2,3)

# objeto da classe - atributo
ev = Evento()
print(ev.nome, ev.local)

a = ev.metodo_instancia()
b = ev.metodo_classe()
c = ev.metodo_estatico()

print(a)
print(b)
print(c)