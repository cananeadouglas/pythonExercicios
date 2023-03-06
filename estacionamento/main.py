import datetime

# Define o número total de vagas do estacionamento
NUM_VAGAS = 100

# Cria um dicionário para armazenar as informações dos veículos estacionados
# A chave é a placa do veículo e o valor é uma lista com a data e hora de entrada, data e hora de saída e tempo de permanência em minutos
estacionamento = {}

def calcular_tempo_permanencia(entrada, saida):
    """Calcula o tempo de permanência em minutos a partir das datas e horas de entrada e saída"""
    tempo_permanencia = saida - entrada
    return int(tempo_permanencia.total_seconds() / 60)

def calcular_valor_pagamento(tempo_permanencia):
    """Calcula o valor a ser pago a partir do tempo de permanência em minutos"""
    valor_hora = 5
    return valor_hora * int(tempo_permanencia / 60)

def registrar_entrada(placa):
    """Registra a entrada de um veículo no estacionamento"""
    if placa in estacionamento:
        print(f"O veículo com placa {placa} já está estacionado.")
    elif len(estacionamento) >= NUM_VAGAS:
        print("O estacionamento está lotado.")
    else:
        entrada = datetime.datetime.now()
        estacionamento[placa] = [entrada, None, None]

def registrar_saida(placa):
    """Registra a saída de um veículo do estacionamento"""
    if placa not in estacionamento:
        print(f"O veículo com placa {placa} não está estacionado.")
    else:
        entrada, saida, tempo_permanencia = estacionamento[placa]
        if saida is not None:
            print(f"O veículo com placa {placa} já saiu do estacionamento.")
        else:
            saida = datetime.datetime.now()
            tempo_permanencia = calcular_tempo_permanencia(entrada, saida)
            valor_pagamento = calcular_valor_pagamento(tempo_permanencia)
            estacionamento[placa] = [entrada, saida, tempo_permanencia, valor_pagamento]
            salvar_dados()
            print(f"O veículo com placa {placa} permaneceu estacionado por {tempo_permanencia} minutos e deve pagar R$ {valor_pagamento:.2f}.")

def salvar_dados():
    """Salva os dados dos veículos estacionados em um arquivo txt"""
    with open("estacionamento.txt", "w") as arquivo:
        for placa, dados in estacionamento.items():
            entrada, saida, tempo_permanencia, valor_pagamento = dados
            if saida is not None:
                linha = f"{placa} {entrada} {saida} {tempo_permanencia} {valor_pagamento}\n"
            else:
                linha = f"{placa} {entrada} None None None\n"
            arquivo.write(linha)

def carregar_dados():
    """Carrega os dados dos veículos estacionados a partir do arquivo txt"""
    try:
        with open("estacionamento.txt", "r") as arquivo:
            for linha in arquivo:
                placa, entrada_str, saida_str, tempo_permanencia_str, valor_pagamento_str = linha.split()
                entrada = datetime.datetime.fromisoformat(entrada_str)
                if saida is not None:
                    saida = datetime.datetime.fromisoformat(saida_str)
                    tempo_permanencia = int(tempo_permanencia_str)
                    valor_pagamento = float(valor_pagamento_str)
                    estacionamento[placa] = [entrada, saida, tempo_permanencia, valor_pagamento]
                else:
                    estacionamento[placa] = [entrada, None, None]
    except FileNotFoundError:
        pass
    
# Carrega os dados dos veículos estacionados do arquivo txt ao iniciar o programa
carregar_dados()

#Loop principal do programa
while True:
    print()
    print("=== GERENCIADOR DE ESTACIONAMENTO ===")
    print("1 - Registrar entrada de veículo")
    print("2 - Registrar saída de veículo")
    print("3 - Exibir lista de veículos estacionados")
    print("4 - Sair do programa")
    
    opcao = input("Digite o número da opção desejada: ")
    if opcao == "1":
        placa = input("Digite a placa do veículo: ")
        registrar_entrada(placa)
    elif opcao == "2":
        placa = input("Digite a placa do veículo: ")
        registrar_saida(placa)
    elif opcao == "3":
        print("=== LISTA DE VEÍCULOS ESTACIONADOS ===")
        for placa, dados in estacionamento.items():
            entrada, saida, tempo_permanencia, valor_pagamento = dados
            if saida is not None:
                print(f"Placa: {placa} - Entrada: {entrada} - Saída: {saida} - Tempo de permanência: {tempo_permanencia} minutos - Valor pago: R$ {valor_pagamento:.2f}")
            else:
                print(f"Placa: {placa} - Entrada: {entrada} - Veículo ainda está estacionado.")
    elif opcao == "4":
        break
    else:
        print("Opção inválida.")
        
#Salva os dados dos veículos estacionados no arquivo txt ao encerrar o programa

salvar_dados()

print("Programa encerrado.")
