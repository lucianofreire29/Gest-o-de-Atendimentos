import customtkinter as ctk
from constantes.cores import *


class CardForm(ctk.CTkFrame):
    def __init__(self, parent, app):
        super().__init__(
            parent,
            border_width=2,
            border_color=AZUL_FONTE_TEXTO,
            fg_color="white"
        )

        self.app = app

        # ===== CONTAINER PRINCIPAL =====
        self.container = ctk.CTkFrame(self, fg_color="white")
        self.container.pack(fill="both", expand=True, padx=10, pady=10)

        # GRID (3 colunas)
        self.container.grid_columnconfigure((0, 1, 2), weight=1)

        self.carregar_dashboard()

    # ===== CARD PADRÃO =====
    def criar_card(self, parent, titulo, valor):
        frame = ctk.CTkFrame(
            parent,
            border_width=2,
            border_color=AZUL_FONTE_TEXTO
        )

        ctk.CTkLabel(
            frame,
            text=titulo,
            text_color=AZUL_FONTE_TEXTO
        ).pack(pady=5)

        ctk.CTkLabel(
            frame,
            text=str(valor),
            font=("Arial", 40),
            text_color=AZUL_FONTE_TEXTO
        ).pack(pady=10)

        return frame

    # ===== DASHBOARD =====
    def carregar_dashboard(self):
        from utils.funçoes import (
            obter_estatisticas_dashboard,
            criar_grafico_pizza,
            criar_grafico_barras
        )

        dados = obter_estatisticas_dashboard()

        # ===== CARDS TOPO =====
        card1 = self.criar_card(
            self.container,
            "Pacientes",
            dados["total_pacientes"]
        )

        card2 = self.criar_card(
            self.container,
            "Atendimentos",
            dados["total_atendimentos"]
        )

        card3 = self.criar_card(
            self.container,
            "Hoje",
            dados["atendimentos_hoje"]
        )

        card1.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        card2.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
        card3.grid(row=0, column=2, padx=10, pady=10, sticky="nsew")

        # ===== GRAFICO ESQUERDA (PIZZA) =====
        frame_esquerda = ctk.CTkFrame(self.container)
        frame_esquerda.grid(
            row=1,
            column=0,
            columnspan=2,
            padx=10,
            pady=10,
            sticky="nsew"
        )

        criar_grafico_pizza(frame_esquerda, dados["genero"])

        # ===== GRAFICO DIREITA (BARRAS) =====
        frame_direita = ctk.CTkFrame(self.container)
        frame_direita.grid(
            row=1,
            column=2,
            padx=10,
            pady=10,
            sticky="nsew"
        )

        criar_grafico_barras(
            frame_direita,
            dados["atendimentos_hoje"],
            dados["atendimentos_ontem"]
        )

    # ===== ATUALIZAR DASHBOARD =====
    def atualizar_dashboard(self):
        for widget in self.container.winfo_children():
            widget.destroy()

        self.carregar_dashboard()