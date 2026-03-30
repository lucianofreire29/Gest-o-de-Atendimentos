import customtkinter as ctk
from tkinter import messagebox
from constantes.cores import *
from utils.funçoes import criar_botao_menu,abrir_cadastro_paciente ,abrir_treeview
from PIL import Image
from cards_frame.card_form import CardForm
from cards_frame.cadastrar_paciente import CadastrarPaciente


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Caresync")
        self.geometry("920x600")
        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("blue")
        self.resizable(False, False)

        # ===== TOPO =====
        self.frame_topo = ctk.CTkFrame(self, fg_color=AZUL_MENU, height=40)
        self.frame_topo.pack(fill="x", side="top")

        # ===== CONTAINER PRINCIPAL =====
        self.frame_main = ctk.CTkFrame(self)
        self.frame_main.pack(fill="both", expand=True)

        # ===== MENU LATERAL =====
        self.frame_menu = ctk.CTkFrame(self.frame_main, fg_color=CINZA_MENU_LATERAL, width=200)
        self.frame_menu.pack(side="left", fill="y")

        self.logo_img = ctk.CTkImage(light_image=Image.open("./assets/caresync.png"),
        size=(160, 160))  # ajuste o tamanho



        self.logo_label = ctk.CTkLabel(self.frame_menu, image=self.logo_img,text=" ")
        self.logo_label.pack()


        criar_botao_menu(self.frame_menu,"Dashboard")
        criar_botao_menu(self.frame_menu,"Pacientes",lambda:abrir_treeview(self))
        criar_botao_menu(self.frame_menu,"Atendimentos")
        criar_botao_menu(self.frame_menu,"Novo Paciente",lambda: abrir_cadastro_paciente(self))
        criar_botao_menu(self.frame_menu,"Novo Atendimento")


        # ===== CONTEÚDO (FORM) =====
        self.frame_form = ctk.CTkFrame(self.frame_main,fg_color="white")
        self.frame_form.pack(side="right", fill="both", expand=True)

        self.card = CardForm(self.frame_form)
        self.card.pack(padx=20, pady=20, fill="both", expand=True)