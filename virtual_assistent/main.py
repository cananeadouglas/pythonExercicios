import datetime
from funcao_aleatorias import falar, adicionar_tarefa, ler_tarefas

# definir o nome da assistente virtual
nome_assistente = "Milena a sua mocinha gostosa."

# obter a data e hora atual
agora = datetime.datetime.now()

# perguntar ao usuário o que ele quer fazer
falar(f"Olá, Douglas, eu sou a {nome_assistente}. O que você gostaria de fazer?")
falar("Você pode me pedir para adicionar uma tarefa ao seu calendário ou para ler suas tarefas agendadas.")

while True:
    comando = input("> ").lower()

    if "adicionar" in comando:
        falar("Para que dia e hora você gostaria de agendar a tarefa?")
        falar("Por favor, digite o dia no formato DD/MM/YYYY e a hora no formato HH:MM.")
        data_hora = input("> ")
        dia, hora = data_hora.split()
        tarefa = comando.split("adicionar", 1)[1].strip()
        adicionar_tarefa(dia, hora, tarefa)

    elif "ler" in comando:
        ler_tarefas()
    
    elif "cantar" in comando:
        pass

    elif "sair" in comando:
        falar("Até mais!")
        break

    else:
        falar("Desculpe, eu não entendi o que você disse. Por favor, tente novamente.")