class Computador:
    def __init__(self, marc, ram, video):
        self.marca = marc
        self.memoria_ram = ram
        self.placa_video = video
    pass

    def Ligar(self, ):
        print ('estou ligando')
    
    def Desligar(self, ):
        print ('estou desligando')
    
    def ExibirInfor(self):
        print(self.marca, self.memoria_ram, self.placa_video)

# Instancias
comp1 = Computador('dell', '8gb', '32gb')
print(comp1.marca, comp1.memoria_ram, comp1.placa_video)
comp1.Ligar()
comp1.Desligar()
comp1.ExibirInfor()
