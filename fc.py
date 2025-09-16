import customtkinter as ctk
import tkinter as tk  # Para StringVar

# Perguntas e respostas
quiz = [
    {
        "pergunta": "Qual é a linguagem usada no back-end do Flask?",
        "alternativas": ["A) Python", "B) Java", "C) HTML"],
        "correta": "A"
    },
    {
        "pergunta": "Qual destes é um loop em Python?",
        "alternativas": ["A) if", "B) for", "C) def"],
        "correta": "B"
    },
    {
        "pergunta": "Qual função exibe algo no terminal?",
        "alternativas": ["A) echo()", "B) write()", "C) print()"],
        "correta": "C"
    }
]

# Estado do quiz
indice_atual = 0

def criar_interface():
    global app, resposta_selecionada, label_pergunta, radio1, radio2, radio3, resultado

    # Cria a janela principal
    ctk.set_appearance_mode("light")
    ctk.set_default_color_theme("blue")
    app = ctk.CTk()
    app.geometry("500x400")
    app.title("Quiz - Múltipla Escolha")

    # Agora pode criar o StringVar (depois da janela)
    resposta_selecionada = tk.StringVar()

    label_pergunta = ctk.CTkLabel(app, text="", font=("Arial", 18), wraplength=450)
    label_pergunta.pack(pady=20)

    radio1 = ctk.CTkRadioButton(app, text="", variable=resposta_selecionada, value="A")
    radio1.pack(anchor="w", padx=40)

    radio2 = ctk.CTkRadioButton(app, text="", variable=resposta_selecionada, value="B")
    radio2.pack(anchor="w", padx=40)

    radio3 = ctk.CTkRadioButton(app, text="", variable=resposta_selecionada, value="C")
    radio3.pack(anchor="w", padx=40)

    botao_verificar = ctk.CTkButton(app, text="Verificar Resposta", command=verificar_resposta)
    botao_verificar.pack(pady=10)

    resultado = ctk.CTkLabel(app, text="", font=("Arial", 16))
    resultado.pack(pady=5)

    botao_proximo = ctk.CTkButton(app, text="Próxima Pergunta", command=proxima_pergunta)
    botao_proximo.pack(pady=5)

    atualizar_pergunta()
    app.mainloop()

def atualizar_pergunta():
    pergunta = quiz[indice_atual]["pergunta"]
    alternativas = quiz[indice_atual]["alternativas"]
    resposta_selecionada.set("")

    label_pergunta.configure(text=pergunta)
    radio1.configure(text=alternativas[0])
    radio2.configure(text=alternativas[1])
    radio3.configure(text=alternativas[2])
    resultado.configure(text="")

def verificar_resposta():
    resposta = resposta_selecionada.get()
    correta = quiz[indice_atual]["correta"]
    if resposta == correta:
        resultado.configure(text="✅ Resposta correta!", text_color="green")
    else:
        resultado.configure(text=f"❌ Errado! Resposta certa: {correta})", text_color="red")

def proxima_pergunta():
    global indice_atual
    indice_atual = (indice_atual + 1) % len(quiz)
    atualizar_pergunta()

# Chama o app
criar_interface()
