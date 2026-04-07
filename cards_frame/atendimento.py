import customtkinter as ctk
from constantes.cores import *
from utils.funçoes import *

class Atendimento(ctk.CTkFrame):
    def __init__(self, parent, app):
        super().__init__(parent, fg_color="white")

        self.app = app

        # FRAME PRINCIPAL
        container = ctk.CTkFrame(self, fg_color="white", border_width=2, border_color=AZUL_FONTE_TEXTO)
        container.pack(fill="both", expand=True, padx=20, pady=20)

        # ===== LADO ESQUERDO =====
        left = ctk.CTkFrame(container, fg_color="white")
        left.pack(side="left", fill="both", expand=True, padx=10, pady=10)

        # TÍTULO
        ctk.CTkLabel(
            left,
            text="Registrar Atendimento",
            text_color=AZUL_FONTE_TEXTO,
            font=("Arial", 28, "bold")
        ).pack(pady=10)

        # BUSCA
        self.entry_busca = ctk.CTkEntry(left, placeholder_text="Pesquisar paciente...")
        self.entry_busca.pack(fill="x", padx=10, pady=5)
        self.entry_busca.bind("<KeyRelease>", self.atualizar_lista)

        # COMBOBOX
        self.combo_paciente = ctk.CTkComboBox(left, values=list(obter_pacientes_dict().keys()))
        self.combo_paciente.pack(fill="x", padx=10, pady=5)

            # 🔥 PREENCHER PACIENTE AUTOMATICAMENTE
        if hasattr(self.app, "paciente_selecionado"):
            paciente = self.app.paciente_selecionado
            self.combo_paciente.set(paciente[1])  # nome do paciente

        # OPCIONAL: travar o campo
        self.combo_paciente.configure(state="disabled")
        del self.app.paciente_selecionado


        # DATA
        self.entry_data = date_entry_cadastro(left)
        self.entry_data.pack(fill="x")

        # TIPO
        self.entry_tipo = entry_cadastro(left, "Tipo de atendimento")
        self.entry_tipo.pack(pady=5)

        # STATUS
        self.status = ctk.StringVar(value="Realizado")

        ctk.CTkRadioButton(left, text="Realizado", variable=self.status, value="Realizado").pack(anchor="w", padx=10)
        ctk.CTkRadioButton(left, text="Em acompanhamento", variable=self.status, value="Em acompanhamento").pack(anchor="w", padx=10)

        # ===== LADO DIREITO =====
        right = ctk.CTkFrame(container, fg_color="white")
        right.pack(side="right", fill="both", expand=True, padx=10, pady=10)

        ctk.CTkLabel(
            right,
            text="Observações",
            text_color=AZUL_FONTE_TEXTO
        ).pack()

        self.text_obs = ctk.CTkTextbox(right, height=300,corner_radius=2,border_width=2)
        self.text_obs.pack(fill="both", expand=True, padx=10, pady=10)

        # BOTÃO
        ctk.CTkButton(
            self,
            text="Registrar Atendimento",
            command=lambda: cadastrar_atendimento(self)
        ).pack(pady=10)

    # atualizar combobox
    def atualizar_lista(self, event):
        termo = self.entry_busca.get()
        nomes = filtrar_pacientes(termo)
        self.combo_paciente.configure(values=nomes)

    def limpar_campos(self):
        self.combo_paciente.set("")
        self.entry_data.delete(0, "end")
        self.entry_tipo.delete(0, "end")
        self.text_obs.delete("1.0", "end")


def abrir_atendimento(app):
    from cards_frame.atendimento import Atendimento
    trocar_tela(app, Atendimento)

