import customtkinter as ctk
from constantes.cores import *
from cards_frame.card_form import CardForm
from utils.funçoes import titulo, entry_cadastro,validar_data_entry,validar_telefone,cadastrar_paciente,limpar_campos


class CadastrarPaciente(CardForm):
    def __init__(self, parent,app):
        super().__init__(parent,app)



# titulo 
        self.label_titulo = ctk.CTkLabel(self.scroll,text="Cadastro de Pacientes",text_color=AZUL_FONTE_TEXTO,font=("",16))
        self.label_titulo.pack(pady=10,anchor="center")


        self.nome = titulo(self.scroll,"nome completo")
        self.entry_nome= entry_cadastro(self.scroll,"Digite o nome")

        self.data = titulo(self.scroll,"data de nascimento")
        self.entry_data= entry_cadastro(self.scroll,"DD/MM/AAAA" ,validar_func=validar_data_entry)

        self.telefone = titulo(self.scroll,"telefone")
        self.entry_telefone= entry_cadastro(self.scroll,"Digite o seu telefone",validar_func=validar_telefone)

        self.email = titulo(self.scroll,"E-mail")
        self.entry_email= entry_cadastro(self.scroll,"Digite o seu e-mail")

        self.cpf = titulo(self.scroll,"CPF OU RG")
        self.entry_cpf= entry_cadastro(self.scroll,"Digite seu CPF ou RG")



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