import customtkinter as ctk
from constantes.cores import *







class CardForm (ctk.CTkFrame):
    def __init__(self, parent,app):
        super().__init__(parent,border_width=2,border_color=AZUL_FONTE_TEXTO,fg_color="white")


        # Scroll interno
        self.scroll = ctk.CTkScrollableFrame(self, fg_color="white")
        self.scroll.pack(fill="both", expand=True, padx=10, pady=10)