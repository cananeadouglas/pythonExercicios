class Evento:
    def __init__(self, nome, local="a"):
        self.nome = nome
        self.local = local
    
    def imprime_informacoes(self):
        print("nome do evento", self.nome)
        print("Local do Evento", self.local)
    
    @classmethod
    def cria_evento_online(cls, nome):
        evento = cls(nome, local="www.lojadodouglas.store?n=1")
        return evento

    @staticmethod
    def calcula_limite_pes_area(area):
        if 5 <= area < 10:
            return 5
        elif 10 <= area < 20:
            return 15
        elif area >= 20:
            return 30
        else:
            return 0



ev = Evento("Aulas de Python ev")
ev2 = Evento("aula de python", "Maceió Alagoas")

print(ev.nome, ev.local)

print(ev2.nome, ev2.local)

ev.imprime_informacoes()
ev2.imprime_informacoes()

ev_online = Evento.cria_evento_online("Loja do Douglas")
ev_online.imprime_informacoes()

print("____________________________________")

print(ev.calcula_limite_pes_area(10))
print(ev2.calcula_limite_pes_area(18))