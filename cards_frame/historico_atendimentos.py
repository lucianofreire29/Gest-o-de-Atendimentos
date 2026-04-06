import customtkinter as ctk
from constantes.cores import *
from utils.funçoes import *

class HistoricoAtendimentos(ctk.CTkFrame):
    def __init__(self, parent, app):
        super().__init__(parent, fg_color="white")

        self.app = app

        container = ctk.CTkFrame(self, fg_color="white", border_width=2, border_color=AZUL_FONTE_TEXTO)
        container.pack(fill="both", expand=True, padx=20, pady=20)


        left = ctk.CTkFrame(container, fg_color="white")
        left.pack(side="left", fill="y", padx=10, pady=10)

        ctk.CTkLabel(left, text="Pacientes", text_color=AZUL_FONTE_TEXTO).pack(pady=5)

        self.entry_busca = ctk.CTkEntry(left, placeholder_text="Buscar...")
        self.entry_busca.pack(padx=10, pady=5)
        self.entry_busca.bind("<KeyRelease>", self.atualizar_lista)

        self.lista = ctk.CTkScrollableFrame(left, width=200, height=400)
        self.lista.pack(padx=10, pady=10)


        self.right = ctk.CTkFrame(container, fg_color="white")
        self.right.pack(side="right", fill="both", expand=True, padx=10, pady=10)

        ctk.CTkLabel(
            self.right,
            text="Histórico de Atendimentos",
            text_color=AZUL_FONTE_TEXTO,
            font=("Arial", 20, "bold")
        ).pack(pady=10)

        self.frame_atendimentos = ctk.CTkScrollableFrame(self.right)
        self.frame_atendimentos.pack(fill="both", expand=True, padx=10, pady=10)

        self.carregar_pacientes()


    def carregar_pacientes(self):
        for widget in self.lista.winfo_children():
            widget.destroy()

        pacientes = obter_pacientes_dict()

        for nome, pid in pacientes.items():
            ctk.CTkButton(
                self.lista,
                text=nome,
                fg_color=CINZA_CLARO,
                text_color=AZUL_FONTE_TEXTO,
                command=lambda n=nome, i=pid: self.mostrar_atendimentos(n, i)
            ).pack(fill="x", pady=2)


    def atualizar_lista(self, event):
        termo = self.entry_busca.get().lower()

        for widget in self.lista.winfo_children():
            widget.destroy()

        pacientes = obter_pacientes_dict()

        for nome, pid in pacientes.items():
            if termo in nome.lower():
                ctk.CTkButton(
                    self.lista,
                    text=nome,
                    command=lambda n=nome, i=pid: self.mostrar_atendimentos(n, i)
                ).pack(fill="x", pady=2)


    def mostrar_atendimentos(self, nome, paciente_id):
        for widget in self.frame_atendimentos.winfo_children():
            widget.destroy()

        atendimentos = obter_atendimentos_por_paciente(paciente_id)

        if not atendimentos:
            ctk.CTkLabel(
                self.frame_atendimentos,
                text="Nenhum atendimento encontrado",
                text_color="gray"
            ).pack(pady=20)
            return

        for at in atendimentos:
            card = ctk.CTkFrame(self.frame_atendimentos, fg_color="white", border_width=1)
            card.pack(fill="x", pady=5, padx=5)

            ctk.CTkLabel(card, text=f"Data: {at['data']}", text_color=AZUL_FONTE_TEXTO).pack(anchor="w", padx=10)
            ctk.CTkLabel(card, text=f"Tipo: {at['tipo']}").pack(anchor="w", padx=10)
            ctk.CTkLabel(card, text=f"Status: {at['status']}").pack(anchor="w", padx=10)

            ctk.CTkLabel(card, text="Observações:", text_color=AZUL_FONTE_TEXTO).pack(anchor="w", padx=10)

            ctk.CTkLabel(
                card,
                text=at["observacoes"],
                wraplength=400,
                justify="left"
            ).pack(anchor="w", padx=10, pady=5)