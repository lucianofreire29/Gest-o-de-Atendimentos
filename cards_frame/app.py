import customtkinter as ctk
from tkinter import messagebox
from constantes.cores import *
from utils.funçoes import criar_botao_menu,abrir_cadastro_paciente ,abrir_treeview,abrir_dashboard,abrir_atendimento,abrir_historico
from PIL import Image
from cards_frame.card_form import CardForm
from cards_frame.cadastrar_paciente import CadastrarPaciente
import os

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Caresync")
        self.geometry("920x600")
        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("blue")
        self.resizable(False, False)

        # ===== TOPO =====
        self.frame_topo = ctk.CTkFrame(self, fg_color=AZUL_MENU, height=40,corner_radius=0)
        self.frame_topo.pack(fill="x", side="top")

        # ===== CONTAINER PRINCIPAL =====
        self.frame_main = ctk.CTkFrame(self)
        self.frame_main.pack(fill="both", expand=True)

        # ===== MENU LATERAL =====
        self.frame_menu = ctk.CTkFrame(self.frame_main, fg_color=CINZA_MENU_LATERAL, width=200,corner_radius=0)
        self.frame_menu.pack(side="left", fill="y")

        BASE_DIR = os.path.dirname(os.path.dirname(__file__))
        caminho_img = os.path.join(BASE_DIR, "assets", "caresync.png")

        self.logo_img = ctk.CTkImage(
            light_image=Image.open(caminho_img),
            size=(160, 160))



        self.logo_label = ctk.CTkLabel(self.frame_menu, image=self.logo_img,text=" ")
        self.logo_label.pack()


        criar_botao_menu(self.frame_menu,"Dashboard",lambda:abrir_dashboard(self))
        criar_botao_menu(self.frame_menu,"Pacientes",lambda:abrir_treeview(self))
        criar_botao_menu(self.frame_menu, "Atendimentos", lambda: abrir_historico(self))
        criar_botao_menu(self.frame_menu,"Novo Paciente",lambda:abrir_cadastro_paciente(self))
        criar_botao_menu(self.frame_menu, "Novo Atendimento", lambda: abrir_atendimento(self))


        # ===== CONTEÚDO (FORM) =====
        self.frame_form = ctk.CTkFrame(self.frame_main,fg_color="white")
        self.frame_form.pack(side="right", fill="both", expand=True)

        self.tela_atual = CardForm(self.frame_form,self)
        self.tela_atual.pack(padx=20, pady=20, fill="both", expand=True)
        self.tela_atual = None

