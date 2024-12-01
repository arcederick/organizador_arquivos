import os
import tkinter as tk
from tkinter import filedialog, messagebox

def organizar_pasta():
    # Selecionar o diretório
    caminho = filedialog.askdirectory(title='Selecione a pasta para organizar')
    if not caminho:
        return  # Usuário cancelou a seleção

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

    # Organizando os arquivos
    for arquivo in lista_arquivos:
        nome, extensao = os.path.splitext(f"{caminho}/{arquivo}")
        for pasta in locais:
            if extensao in locais[pasta]:
                # Criar pasta se não existir
                if not os.path.exists(f"{caminho}/{pasta}"):
                    os.mkdir(f"{caminho}/{pasta}")
                # Mover arquivo para a pasta
                os.rename(f"{caminho}/{arquivo}", f"{caminho}/{pasta}/{arquivo}")

    # Exibir mensagem de sucesso
    messagebox.showinfo("Organização Concluída", f"Os arquivos em '{caminho}' foram organizados com sucesso!")

# Configuração da interface gráfica
root = tk.Tk()
root.title("File-O")

# Definir tamanho fixo da janela
janela_largura = 300
janela_altura = 600

# Obter dimensões da tela
largura_tela = root.winfo_screenwidth()
altura_tela = root.winfo_screenheight()

# Calcular posição para centralizar
pos_x = (largura_tela - janela_largura) // 2
pos_y = (altura_tela - janela_altura) // 2

# Aplicar posição centralizada
root.geometry(f"{janela_largura}x{janela_altura}+{pos_x}+{pos_y}")
root.resizable(False, False)  # Impedir redimensionamento

# Adicionar rótulo de boas-vindas
lbl_boas_vindas = tk.Label(
    root, 
    text="Bem-vindo ao File-O!", 
    font=("Arial", 14), 
    pady=10
)
lbl_boas_vindas.pack(pady=(20, 10), padx=20) 

# Texto formatado para exibir como lista
lista_tipos = """\
- Imagens: .png, .jpg, .jpeg, .gif
- Documentos: .pdf, .txt, .docx, .PDF
- Compactados: .zip, .ZIP, .rar
- XML: .xml
- SQL: .sql, .SQL
- Executáveis: .exe
- Planilhas: .xlsx, .xls, .csv\
"""

# Rótulo para exibir a lista de tipos de arquivos
lbl_legenda = tk.Label(
    root, 
    text=f"Os arquivos rastreáveis são:\n\n{lista_tipos}", 
    font=("Arial", 12), 
    justify="left",  # Centraliza o texto
    anchor="w",    # Centraliza dentro do widget
   
    
)
lbl_legenda.pack(pady=20, padx=20)


# Criar botão para iniciar organização
btn_organizar = tk.Button(
    root, 
    text="Selecionar Pasta para Organizar", 
    command=organizar_pasta, 
    width=30,  # Largura do botão
    height=2,  # Altura do botão
    padx=10, 
    pady=5
)
btn_organizar.pack(side=tk.BOTTOM, pady=10)  # Centralizar o botão com espaçamento vertical e bottom

# Iniciar o loop principal
root.mainloop()
