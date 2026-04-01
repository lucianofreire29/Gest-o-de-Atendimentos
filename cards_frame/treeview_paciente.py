import customtkinter as ctk
from tkinter import messagebox
from constantes.cores import *
from cards_frame.card_form import CardForm
from tkinter import ttk
import json
import os
from utils.funçoes import carregar_pacientes, abrir_detalhes_paciente,pesquisar_pacientes


class TreeviewPaciente(ctk.CTkFrame):
    def __init__(self, parent,app):
        super().__init__(parent, fg_color="white")
        self.app = app
        self.pack(fill="both", expand=True)
        
        
        self.entry_pesquisa = ctk.CTkEntry(
            self,
            placeholder_text="Pesquisar por nome ou telefone..."
        )
        self.entry_pesquisa.pack(padx=10, pady=5, fill="x")

        # evento de digitação
        self.entry_pesquisa.bind(
            "<KeyRelease>",
            lambda event: pesquisar_pacientes(
                self.treeview_paciente,
                self.entry_pesquisa.get()
            )
        )

        #  FRAME NORMAL (substitui o scroll)
        frame_tabela = ctk.CTkFrame(self, fg_color="white")
        frame_tabela.pack(fill="both", expand=True, padx=10, pady=10)

        #  controle de expansão
        frame_tabela.grid_rowconfigure(0, weight=1)
        frame_tabela.grid_columnconfigure(0, weight=1)

        # Treeview
        self.treeview_paciente = ttk.Treeview(
            frame_tabela,
            columns=("ID", "Nome", "Data de Nascimento", "email", "Telefone", "CPF/RG", "Genero"),
            show="headings"
        )

        for col in self.treeview_paciente["columns"]:
            self.treeview_paciente.heading(col, text=col)

        self.treeview_paciente.column("ID", width=20)
        self.treeview_paciente.column("Nome", width=150)
        self.treeview_paciente.column("Data de Nascimento", width=100)
        self.treeview_paciente.column("email", width=120)
        self.treeview_paciente.column("Telefone", width=100)
        self.treeview_paciente.column("CPF/RG", width=100)
        self.treeview_paciente.column("Genero", width=80)

        # Scrollbar do próprio Treeview
        scrollbar = ttk.Scrollbar(
            frame_tabela,
            orient="vertical",
            command=self.treeview_paciente.yview
        )
        self.treeview_paciente.configure(yscrollcommand=scrollbar.set)

        # 🔥 layout correto
        self.treeview_paciente.grid(row=0, column=0, sticky="nsew")
        scrollbar.grid(row=0, column=1, sticky="ns")

        # Evento de duplo clique
        self.treeview_paciente.bind(
            "<Double-1>",
            lambda event: abrir_detalhes_paciente(self.treeview_paciente, self, event, self.app))


        # Carrega os pacientes
        carregar_pacientes(self.treeview_paciente)