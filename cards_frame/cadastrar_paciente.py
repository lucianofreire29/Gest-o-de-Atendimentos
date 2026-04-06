import customtkinter as ctk
from constantes.cores import *
from cards_frame.card_form import CardForm
from utils.funçoes import titulo, entry_cadastro,validar_data_entry,validar_telefone,cadastrar_paciente,limpar_campos,date_entry_cadastro


class CadastrarPaciente(CardForm):
    def __init__(self, parent,app):
        super().__init__(parent,app)



# titulo 
        self.label_titulo = ctk.CTkLabel(self.scroll,text="Cadastro de Pacientes",text_color=AZUL_FONTE_TEXTO,font=("",16))
        self.label_titulo.pack(pady=10,anchor="center")

        frame_nome = ctk.CTkFrame(self.scroll, fg_color="transparent")
        frame_nome.pack(fill="x", padx=20, pady=5)

        self.nome = titulo(frame_nome, "Nome completo")
        self.nome.pack(anchor="w")

        self.entry_nome = entry_cadastro(frame_nome, "Digite o nome")
        self.entry_nome.pack(fill="x")

        frame_linha = ctk.CTkFrame(self.scroll, fg_color="transparent")
        frame_linha.pack(fill="x", padx=20, pady=5)

        # DATA
        frame_data = ctk.CTkFrame(frame_linha, fg_color="transparent")
        frame_data.pack(side="left", expand=True, fill="x", padx=5)

        self.data = titulo(frame_data, "Data de nascimento")
        self.data.pack(anchor="w")

        self.entry_data = date_entry_cadastro(frame_data)
        self.entry_data.pack(fill="x")

        # CPF
        frame_cpf = ctk.CTkFrame(frame_linha, fg_color="transparent")
        frame_cpf.pack(side="left", expand=True, fill="x", padx=5)

        self.cpf = titulo(frame_cpf, "CPF ou RG")
        self.cpf.pack(anchor="w")

        self.entry_cpf = entry_cadastro(frame_cpf, "Digite seu CPF ou RG")
        self.entry_cpf.pack(fill="x")

        frame_contato = ctk.CTkFrame(self.scroll, fg_color="transparent")
        frame_contato.pack(fill="x", padx=20, pady=5)

        # TELEFONE
        frame_tel = ctk.CTkFrame(frame_contato, fg_color="transparent")
        frame_tel.pack(side="left", expand=True, fill="x", padx=5)

        self.telefone = titulo(frame_tel, "Telefone")
        self.telefone.pack(anchor="w")

        self.entry_telefone = entry_cadastro(frame_tel, "Digite o telefone", validar_func=validar_telefone)
        self.entry_telefone.pack(fill="x")

        # EMAIL
        frame_email = ctk.CTkFrame(frame_contato, fg_color="transparent")
        frame_email.pack(side="left", expand=True, fill="x", padx=5)

        self.email = titulo(frame_email, "E-mail")
        self.email.pack(anchor="w")

        self.entry_email = entry_cadastro(frame_email, "Digite o e-mail")
        self.entry_email.pack(fill="x")



        self.genero = ctk.CTkComboBox(
        self.scroll,
        values=["Masculino", "Feminino", "Outro"]
        )
        self.genero.pack(pady=5)


# frame para os botões
        frame_botoes = ctk.CTkFrame(self.scroll, fg_color="transparent")
        frame_botoes.pack(pady=10)

        btn_cadastrar = ctk.CTkButton(frame_botoes,text="cadastrar",fg_color=AZUL_BOTÃO,text_color="white",border_width=2,command=lambda: cadastrar_paciente(self))
        btn_cadastrar.pack(side="left", padx=5)

        btn_limpar = ctk.CTkButton(frame_botoes,text="Limpar",fg_color=AZUL_BOTÃO,text_color="white",border_width=2,command=lambda: limpar_campos(self))
        btn_limpar.pack(side="left", padx=5)