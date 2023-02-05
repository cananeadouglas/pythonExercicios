class Evento:
    # variavel da classe evento
    id = 1
    
    def __init__(self, nome, local="a"):
        self.nome = nome
        self.local = local
        self.id = Evento.id  # atributo de instância
        Evento.id += 1  # atributo de classe
        
    def imprime_informacoes(self):
        print(f"ID do evento {self.id}")
        print(f"nome do evento {self.nome}")
        print(f"Local do Evento {self.local}")
        print("____________________________________")
    
    @classmethod
    def cria_evento_online(cls, nome):
        evento = cls(nome, local=f"www.lojadodouglas.store?n={cls.id}")
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



ev = Evento("aulas a noite de sábado")
ev2 = Evento("aula de python", "Maceió Alagoas")

print(ev.nome, ev.local)
print(ev2.nome, ev2.local)

ev.imprime_informacoes()
ev2.imprime_informacoes()


ev_online = Evento.cria_evento_online("Loja do Douglas")
ev_online.imprime_informacoes()

print("____________________________________")

print(ev.calcula_limite_pes_area(9))
print(ev2.calcula_limite_pes_area(18))
print(ev_online.id)
