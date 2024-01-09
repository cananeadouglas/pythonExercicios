from customtkinter import *
from PIL import Image
from tkinter import *
from tkinter import ttk, messagebox
import keyboard

count = 0

def atualizar():
    #messagebox.showinfo(title="atenção", message="você me clicou")
    #print("botão clicado")
    global count
    count += 1
    label.configure(text=f'você clicou no botão {count} vezes')


app = CTk()
app.geometry("500x400")
set_appearance_mode("dark")

#Button
btn = CTkButton(master=app, text="Clique", corner_radius=32, fg_color="#C850C0", hover_color="#4158D0")
#btn.bind("<Button-3>", atualizar) # botão direito <Button-3>, Passar por cima <Enter>
btn.place(relx=0.5, rely=0.5, anchor="center", relwidth=0.21, relheight=0.07)

outro_btn = CTkButton(master=app, text="clique para contabilizar", command=atualizar)
outro_btn.pack(anchor="n", expand=True,)
entry = CTkEntry(master=app, placeholder_text='digite seu nome aqui...',)
entry.place(relx=0.4, rely=0.6, relwidth=0.21, relheight=0.07)

label = CTkLabel(master=app, text='clique no button 0 times')
label.pack(anchor="s", expand=True, pady=10)

app.mainloop()