import customtkinter as ctk
import json
import os
from CTkMessagebox import CTkMessagebox
from constantes.cores import *
from PIL import Image
import os


BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
CAMINHO_USUARIOS = os.path.join(DATA_DIR, "usuarios.json")

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
caminho_logo = os.path.join(BASE_DIR, "assets", "caresyncfundo.png")

img = Image.open(caminho_logo)
logo_img = ctk.CTkImage(img, size=(160, 160))




import customtkinter as ctk
import json
import os
from CTkMessagebox import CTkMessagebox
from constantes.cores import *
from PIL import Image

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
CAMINHO_USUARIOS = os.path.join(DATA_DIR, "usuarios.json")


class Login(ctk.CTkFrame):
    def __init__(self, parent, app):
        super().__init__(parent)

        self.app = app
        self.configure(fg_color=BRANCO_FUNDO)

        #  CONTAINER CENTRAL 
        container = ctk.CTkFrame(self, fg_color="white", corner_radius=15)
        container.place(relx=0.5, rely=0.5, anchor="center")

        #  LOGO 
        caminho_logo = os.path.join(BASE_DIR, "assets", "caresyncfundo.png")

        if os.path.exists(caminho_logo):
            img = Image.open(caminho_logo)
            logo_img = ctk.CTkImage(img, size=(140, 140))

            ctk.CTkLabel(container, image=logo_img, text="").pack(pady=(20, 10))
            self.logo_ref = logo_img  # evita bug de imagem sumir

        #  TÍTULO 
        ctk.CTkLabel(
            container,
            text="Login do Sistema",
            text_color=AZUL_FONTE_TEXTO,
            font=("Arial", 18, "bold")
        ).pack(pady=10)

        #  USUÁRIO 
        self.entry_user = ctk.CTkEntry(
            container,
            placeholder_text="Usuário",
            width=250
        )
        self.entry_user.pack(pady=10)

        #  SENHA 
        self.entry_senha = ctk.CTkEntry(
            container,
            placeholder_text="Senha",
            show="*",
            width=250
        )
        self.entry_senha.pack(pady=10)

        #  BOTÃO 
        ctk.CTkButton(
            container,
            text="Entrar",
            fg_color=AZUL_BOTÃO,
            hover_color=AZUL_MENU,
            command=self.verificar_login
        ).pack(pady=20)

    def verificar_login(self):
        usuario = self.entry_user.get()
        senha = self.entry_senha.get()

        if not os.path.exists(CAMINHO_USUARIOS):
            CTkMessagebox(title="Erro", message="Arquivo de usuários não encontrado", icon="cancel")
            return

        with open(CAMINHO_USUARIOS, "r", encoding="utf-8") as f:
            usuarios = json.load(f)

        for u in usuarios:
            if u["usuario"] == usuario and u["senha"] == senha:
                CTkMessagebox(title="Sucesso", message="Login realizado com sucesso!", icon="check")

                self.app.mostrar_menu()

                from utils.funçoes import abrir_dashboard
                abrir_dashboard(self.app)
                return

        CTkMessagebox(title="Erro", message="Usuário ou senha inválidos", icon="cancel")