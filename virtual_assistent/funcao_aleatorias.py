import pyttsx3

# configurar a engine text-to-speech
engine = pyttsx3.init()

# função para a assistente dizer uma mensagem
def falar(mensagem):
    engine.say(mensagem)
    engine.runAndWait()

# função para adicionar uma tarefa ao seu calendário
def adicionar_tarefa(dia, hora, tarefa):
    with open('calendario.txt', 'a') as arquivo:
        arquivo.write(f"{dia} {hora} - {tarefa}\n")
    falar(f"OK, adicionado {tarefa} para {dia} às {hora}.")

# função para ler as tarefas do seu calendário
def ler_tarefas():
    with open('calendario.txt', 'r') as arquivo:
        tarefas = arquivo.readlines()
    if tarefas:
        falar("Você tem as seguintes tarefas agendadas:")
        for tarefa in tarefas:
            falar(tarefa)
    else:
        falar("Você não tem nenhuma tarefa agendada.")