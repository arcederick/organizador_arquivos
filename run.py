import os
import tkinter as tk
from tkinter import filedialog, messagebox, font as tkfont

def organizar_pasta():
    caminho = filedialog.askdirectory(title='Selecione a pasta para organizar')
    if not caminho:
        return

    lista_arquivos = os.listdir(caminho)
    locais = {
        "Imagens": [".png", ".jpg", ".jpeg", ".gif"],
        "Documentos": [".pdf", ".txt", ".docx", ".PDF"],
        "Compactados": [".zip", ".ZIP", ".rar"],
        "XML": [".xml"],
        "SQL": [".sql", ".SQL"],
        "Exe": [".exe"],
        "Planilhas": [".xlsx", ".xls", ".csv"]
    }

    for arquivo in lista_arquivos:
        nome, extensao = os.path.splitext(f"{caminho}/{arquivo}")
        for pasta in locais:
            if extensao in locais[pasta]:
                if not os.path.exists(f"{caminho}/{pasta}"):
                    os.mkdir(f"{caminho}/{pasta}")
                os.rename(f"{caminho}/{arquivo}", f"{caminho}/{pasta}/{arquivo}")

    messagebox.showinfo("Organização Concluída", f"Os arquivos em '{caminho}' foram organizados com sucesso! Volte ao diretório e confira :D")


##################################################
##################################################
##################################################
##################################################
# Interface Gráfica com Tkinter

# criado canvas para manipular bordas
def criar_frame_arredondado(master, width, height, bg, border_radius=20):
    canvas = tk.Canvas(master, width=width, height=height, bg=master["bg"], highlightthickness=0)
    canvas.pack_propagate(False)

    x1, y1, x2, y2 = 10, 10, width - 10, height - 10
    r = border_radius
    canvas.create_arc(x1, y1, x1 + 2 * r, y1 + 2 * r, start=90, extent=90, fill=bg, outline="")
    canvas.create_arc(x2 - 2 * r, y1, x2, y1 + 2 * r, start=0, extent=90, fill=bg, outline="")
    canvas.create_arc(x1, y2 - 2 * r, x1 + 2 * r, y2, start=180, extent=90, fill=bg, outline="")
    canvas.create_arc(x2 - 2 * r, y2 - 2 * r, x2, y2, start=270, extent=90, fill=bg, outline="")
    canvas.create_rectangle(x1 + r, y1, x2 - r, y2, fill=bg, outline="")
    canvas.create_rectangle(x1, y1 + r, x2, y2 - r, fill=bg, outline="")
    return canvas


# Configuração da interface gráfica
root = tk.Tk()
root.title("File-O")
root.geometry("450x700")  # Tamanho da janela
root.configure(bg="#5DBBC7")  # Fundo App
root.resizable(False, False)

# Centralizar a janela na tela
largura_tela = root.winfo_screenwidth()  # Largura da tela
altura_tela = root.winfo_screenheight()  # Altura da tela
largura_janela = 450  # Largura da janela
altura_janela = 720  # Altura da janela

# Calcular a posição para centralizar
pos_x = (largura_tela - largura_janela) // 2
pos_y = (altura_tela - altura_janela) // 2

# Aplicar a posição calculada
root.geometry(f"{largura_janela}x{altura_janela}+{pos_x}+{pos_y}")

# Usando uma fonte padrão instalada no sistema
font_family = "Montserrat"  
try:
    test_font = tkfont.nametofont("TkDefaultFont").actual()
    font_family = test_font["family"] if "Montserrat" not in test_font["family"] else font_family
except:
    font_family = "Arial"

# Adicionar título
lbl_titulo = tk.Label(
    root,
    text="Bem-vindo ao File-O!",
    font=(font_family, 22, "bold"),
    bg="#5DBBC7",
    fg="#FFFFFF",
    pady=10
)
lbl_titulo.pack(pady=(20, 10))

# Texto descritivo
lbl_texto = tk.Label(
    root,
    text="Organize seus arquivos de forma rápida e prática.",
    font=(font_family, 14),
    bg="#5DBBC7",
    fg="#FFFFFF",
    wraplength=400,
    justify="center"
)
lbl_texto.pack(pady=(10, 20))

# Area branca no centro para exibir a lista de tipos de arquivos
frame_lista = criar_frame_arredondado(root, width=350, height=400, bg="#FFFFFF", border_radius=10)
frame_lista.pack(pady=20)
frame_lista.pack_propagate(False)

# Adicionar título dentro do frame
lbl_lista_titulo = tk.Label(
    frame_lista,
    text="Arquivos Rastreáveis",
    font=(font_family, 16, "bold"),
    bg="#DDD569",
    fg="#000000",
    pady=10
)
lbl_lista_titulo.pack()

# Adicionar lista de tipos de arquivos
lista_tipos = """\
Imagens: png, jpg, jpeg, gif

Documentos: pdf, txt, docx

Compactados: zip, rar

XML: xml

SQL: sql

Executáveis: exe

Planilhas: xlsx, xls, .csv
"""
lbl_lista = tk.Label(
    frame_lista,
    text=lista_tipos,
    font=(font_family, 12),
    bg="#FFFFFF",
    fg="#000000",
    justify="left",
    anchor="w",
    wraplength=350
)
lbl_lista.pack(padx=10, pady=10)

# Funções para o efeito de hover
def on_enter(event):
    btn_organizar['bg'] = "#C9C857"  # Cor ao passar o mouse
    btn_organizar['fg'] = "#000000"  # Cor do texto ao passar o mouse
    btn_organizar['cursor'] = "hand2"  # Cursor de mão

def on_leave(event):
    btn_organizar['bg'] = "#DDD569"  # Cor normal do botão
    btn_organizar['fg'] = "#000000"  # Cor normal do texto
    btn_organizar['cursor'] = ""  # Remove o cursor especial

# Botão de ação
btn_organizar = tk.Button(
    root,
    text="Selecionar Pasta para Organizar",
    command=organizar_pasta,
    font=(font_family, 14, "bold"),
    bg="#DDD569",
    fg="#000000",
    activebackground="#DDD569",
    activeforeground="#FFFFFF",
    relief="flat",
    width=30,
    height=2
)
btn_organizar.pack(pady=20)

# Vincular eventos ao botão
btn_organizar.bind("<Enter>", on_enter)  # Quando o mouse entra no botão
btn_organizar.bind("<Leave>", on_leave)  # Quando o mouse sai do botão

# Exibir janela
root.mainloop()
