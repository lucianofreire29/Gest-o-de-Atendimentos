import os

import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
from PIL import Image

from constantes.cores import AZUL_BOTÃO, AZUL_FONTE_TEXTO, AZUL_MENU, BRANCO_FUNDO
from utils.autenticacao import autenticar, credenciais_configuradas
from utils.caminhos import ASSETS_DIR


class Login(ctk.CTkFrame):
    def __init__(self, parent, app):
        super().__init__(parent)
        self.app = app
        self.configure(fg_color=BRANCO_FUNDO)

        container = ctk.CTkFrame(self, fg_color="white", corner_radius=15)
        container.place(relx=0.5, rely=0.5, anchor="center")

        caminho_logo = os.path.join(ASSETS_DIR, "caresyncfundo.png")
        if os.path.exists(caminho_logo):
            imagem = Image.open(caminho_logo)
            self.logo_img = ctk.CTkImage(imagem, size=(140, 140))
            ctk.CTkLabel(container, image=self.logo_img, text="").pack(pady=(20, 10))

        ctk.CTkLabel(container, text="Login do Sistema", text_color=AZUL_FONTE_TEXTO, font=("Arial", 18, "bold")).pack(pady=10)

        self.entry_usuario = ctk.CTkEntry(container, placeholder_text="Usuário", width=250)
        self.entry_usuario.pack(pady=10)

        self.entry_senha = ctk.CTkEntry(container, placeholder_text="Senha", show="*", width=250)
        self.entry_senha.pack(pady=10)
        self.entry_senha.bind("<Return>", lambda _event: self.verificar_login())

        ctk.CTkButton(container, text="Entrar", fg_color=AZUL_BOTÃO, hover_color=AZUL_MENU, command=self.verificar_login).pack(pady=20)

    def verificar_login(self):
        if not credenciais_configuradas():
            CTkMessagebox(title="Configuração necessária", message="Configure CARESYNC_USUARIO e CARESYNC_SENHA no arquivo .env.", icon="warning")
            return

        usuario = self.entry_usuario.get().strip()
        senha = self.entry_senha.get()

        if autenticar(usuario, senha):
            CTkMessagebox(title="Sucesso", message="Login realizado com sucesso!", icon="check")
            self.app.mostrar_menu()
            from utils.funcoes import abrir_dashboard
            abrir_dashboard(self.app)
            return

        self.entry_senha.delete(0, "end")
        CTkMessagebox(title="Erro", message="Usuário ou senha inválidos.", icon="cancel")
