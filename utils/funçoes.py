import customtkinter as ctk
from constantes.cores import *
from datetime import datetime
import json
import os
from CTkMessagebox import CTkMessagebox
from cards_frame.card_form import CardForm



BASE_DIR = os.path.dirname(os.path.dirname(__file__))


DATA_DIR = os.path.join(BASE_DIR, "data")


CAMINHO_PACIENTES = os.path.join(DATA_DIR, "pacientes.json")




def criar_botao_menu(parent, texto, comando=None):
    btn = ctk.CTkButton(
        parent,
        fg_color=CINZA_CLARO,
        border_color=AZUL_FONTE_TEXTO,
        border_width=2,
        text=texto,
        text_color=AZUL_FONTE_TEXTO,
        command=comando,
        hover_color=CINZA_MENU_LATERAL
    )
    btn.pack(pady=10, anchor="center")
    return btn


def abrir_dashboard(app):
    from cards_frame.card_form import CardForm
    trocar_tela(app, CardForm)

def abrir_cadastro_paciente(app):
    from cards_frame.cadastrar_paciente import CadastrarPaciente
    trocar_tela(app, CadastrarPaciente)

def abrir_treeview(app):
    from cards_frame.treeview_paciente import TreeviewPaciente
    trocar_tela(app, TreeviewPaciente)





# função dos textos cadastrar paciente
def titulo(parent, texto):
    return ctk.CTkLabel(parent, text=texto, text_color=AZUL_FONTE_TEXTO)



# função dos entry cadastrar paciente
def entry_cadastro(parent, placeholder, validar_func=None):

    entry = ctk.CTkEntry(
        parent,
        border_color="black",
        placeholder_text=placeholder,
        width=200
    )

    if validar_func:
        vcmd = (parent.register(validar_func), "%P")
        entry.configure(validate="key", validatecommand=vcmd)

    return entry



def validar_data_entry(texto):

    if texto == "":  # permite apagar tudo
        return True
    # permite apenas dígitos ou '/'
    return all(c.isdigit() or c == "/" for c in texto)


# validar data
def validar_data(texto):
    if texto == "":
        return True  

    
    if len(texto) != 10:
        return False

    
    if texto[2] != "/" or texto[5] != "/":
        return False

    try:
        datetime.strptime(texto, "%d/%m/%Y")
        return True
    except ValueError:
        return False


# validação do telefone
def validar_telefone(texto):
    if texto == "":
        return True

    # só números
    if not texto.isdigit():
        return False

    # limite (DDD + número)
    if len(texto) > 11:
        return False

    return True


os.makedirs(DATA_DIR, exist_ok=True)
# salvar pacientes
def salvar_paciente(dados):
    caminho = CAMINHO_PACIENTES
    # se o arquivo não existir, cria lista vazia
    if not os.path.exists(caminho):
        with open(caminho, "w") as f:
            json.dump([], f)

    # lê os dados existentes
    with open(caminho, "r") as f:
        pacientes = json.load(f)

    # gera ID automático
    if pacientes:
        novo_id = pacientes[-1]["id"] + 1
    else:
        novo_id = 1

    dados["id"] = novo_id

    # adiciona novo paciente
    pacientes.append(dados)

    # salva novamente
    with open(caminho, "w") as f:
        json.dump(pacientes, f, indent=4)


# função salvar 
def cadastrar_paciente(self):
    # pega os dados do entry
    dados = {
        "nome": self.entry_nome.get(),
        "data_nascimento": self.entry_data.get(),
        "telefone": self.entry_telefone.get(),
        "email": self.entry_email.get(),
        "cpf/rg": self.entry_cpf.get(),
        "genero": self.genero.get()
    }

    # validação de data
    if not validar_data(dados["data_nascimento"]):
        CTkMessagebox(
            title="Erro",
            message="Data inválida! Use o formato DD/MM/AAAA",
            icon="cancel",
            option_1="OK"
        )
        return

    # validação de nome
    if not dados["nome"]:
        CTkMessagebox(
            title="Erro",
            message="Informe o nome do paciente",
            icon="cancel",
            option_1="OK"
        )
        return

    # salva paciente
    salvar_paciente(dados)

    # sucesso
    CTkMessagebox(
        title="Sucesso",
        message=f"Paciente {dados['nome']} cadastrado com sucesso!",
        icon="check",
        option_1="OK"
    )

    # limpa campos
    limpar_campos(self)


def limpar_campos(self):
    self.entry_nome.delete(0, "end")
    self.entry_data.delete(0, "end")
    self.entry_telefone.delete(0, "end")
    self.entry_email.delete(0, "end")
    self.entry_cpf.delete(0, "end")
    self.genero.set("")




def carregar_pacientes(treeview):
    import json
    import os

    caminho = CAMINHO_PACIENTES

    if not os.path.exists(caminho):
        return

    with open(caminho, "r", encoding="utf-8") as arquivo:
        pacientes = json.load(arquivo)

    # limpa
    for item in treeview.get_children():
        treeview.delete(item)

    
    for paciente in pacientes:
        treeview.insert("", "end", values=(
            paciente.get("id"),
            paciente.get("nome"),
            paciente.get("data_nascimento"),
            paciente.get("email"),
            paciente.get("telefone"),
            paciente.get("cpf/rg"),
            paciente.get("genero")
        ))



def abrir_detalhes_paciente(treeview, treeview_frame, event, app):

    item_id = treeview.identify_row(event.y)
    if not item_id:
        return  

    item = treeview.item(item_id)
    paciente = item["values"]

    renderizar_detalhe(paciente, treeview_frame, treeview, app)




def excluir_paciente(paciente, app):
    caminho = CAMINHO_PACIENTES
    with open(caminho, "r", encoding="utf-8") as f:
        pacientes = json.load(f)

    pacientes = [p for p in pacientes if p["id"] != paciente[0]]  

    with open(caminho, "w", encoding="utf-8") as f:
        json.dump(pacientes, f, indent=4)

    CTkMessagebox(title="Sucesso", message=f"Paciente {paciente[1]} excluído!", icon="check", option_1="OK")

    abrir_treeview(app)

def editar_paciente(paciente, treeview_frame):
    CTkMessagebox(title="Editar", message=f"Editar paciente {paciente[1]}", icon="check", option_1="OK")

def registrar_atendimento(paciente):
    CTkMessagebox(title="Atendimento", message=f"Registrar atendimento para {paciente[1]}", icon="check", option_1="OK")



def editar_paciente(paciente, treeview_frame, treeview_paciente):
    # limpa o frame
    for widget in treeview_frame.winfo_children():
        widget.destroy()

    editar_frame = ctk.CTkFrame(treeview_frame, fg_color="white")
    editar_frame.pack(fill="both", expand=True, padx=20, pady=20)

    entry_dict = {}

    frame_nome = ctk.CTkFrame(editar_frame, fg_color="transparent")
    frame_nome.pack(fill="x", padx=20, pady=5)

    label_nome = ctk.CTkLabel(frame_nome, text="Nome", text_color=AZUL_FONTE_TEXTO)
    label_nome.pack(anchor="w")

    entry_nome = ctk.CTkEntry(frame_nome, border_color="black")
    entry_nome.pack(fill="x")
    entry_nome.insert(0, paciente[1])

    entry_dict["nome"] = entry_nome

    frame_linha = ctk.CTkFrame(editar_frame, fg_color="transparent")
    frame_linha.pack(fill="x", padx=20, pady=5)

    frame_linha.grid_columnconfigure(0, weight=1)
    frame_linha.grid_columnconfigure(1, weight=1)

    # DATA
    frame_data = ctk.CTkFrame(frame_linha, fg_color="transparent")
    frame_data.grid(row=0, column=0, sticky="ew", padx=5)

    label_data = ctk.CTkLabel(frame_data, text="Data de Nascimento", text_color=AZUL_FONTE_TEXTO)
    label_data.pack(anchor="w")

    entry_data = ctk.CTkEntry(frame_data, border_color="black")
    entry_data.pack(fill="x")
    entry_data.insert(0, paciente[2])

    entry_dict["data_de_nascimento"] = entry_data


    # CPF
    frame_cpf = ctk.CTkFrame(frame_linha, fg_color="transparent")
    frame_cpf.grid(row=0, column=1, sticky="ew", padx=5)

    label_cpf = ctk.CTkLabel(frame_cpf, text="CPF/RG", text_color=AZUL_FONTE_TEXTO)
    label_cpf.pack(anchor="w")

    entry_cpf = ctk.CTkEntry(frame_cpf, border_color="black")
    entry_cpf.pack(fill="x")
    entry_cpf.insert(0, paciente[5])

    entry_dict["cpf/rg"] = entry_cpf


    frame_contato = ctk.CTkFrame(editar_frame, fg_color="transparent")
    frame_contato.pack(fill="x", padx=20, pady=5)

    # TELEFONE
    frame_tel = ctk.CTkFrame(frame_contato, fg_color="transparent")
    frame_tel.grid(row=0, column=0, sticky="ew", padx=5)

    label_tel = ctk.CTkLabel(frame_tel, text="Telefone", text_color=AZUL_FONTE_TEXTO)
    label_tel.pack(anchor="w")

    entry_tel = ctk.CTkEntry(frame_tel, border_color="black")
    entry_tel.pack(fill="x")
    entry_tel.insert(0, paciente[4])

    entry_dict["telefone"] = entry_tel

    frame_contato.grid_columnconfigure(0, weight=1)
    frame_contato.grid_columnconfigure(1, weight=1)

    # EMAIL
    frame_email = ctk.CTkFrame(frame_contato, fg_color="transparent")
    frame_email.grid(row=0, column=1, sticky="ew", padx=5)

    label_email = ctk.CTkLabel(frame_email, text="Email", text_color=AZUL_FONTE_TEXTO)
    label_email.pack(anchor="w")

    entry_email = ctk.CTkEntry(frame_email, border_color="black")
    entry_email.pack(fill="x")
    entry_email.insert(0, paciente[3])

    entry_dict["email"] = entry_email

    frame_genero = ctk.CTkFrame(editar_frame, fg_color="transparent")
    frame_genero.pack(fill="x", padx=20, pady=5)

    label_genero = ctk.CTkLabel(frame_genero, text="Gênero", text_color=AZUL_FONTE_TEXTO)
    label_genero.pack(anchor="w")

    combo = ctk.CTkComboBox(frame_genero, values=["Masculino", "Feminino", "Outro"])
    combo.pack(fill="x")
    combo.set(paciente[6])

    entry_dict["genero"] = combo



    # botão salvar
    ctk.CTkButton(
        editar_frame,
        text="Salvar Alterações",
        command=lambda: salvar_edicao(paciente[0], entry_dict, treeview_paciente)
    ).pack(pady=10)

def salvar_edicao(paciente_id, entry_dict, treeview):
    caminho = CAMINHO_PACIENTES

    nome = entry_dict["nome"].get()
    data_nascimento = entry_dict["data_de_nascimento"].get()
    telefone = entry_dict["telefone"].get()
    email = entry_dict["email"].get()
    cpf_rg = entry_dict["cpf/rg"].get()
    genero = entry_dict["genero"].get()

    # validações
    from utils.funçoes import validar_data, validar_telefone
    if not nome:
        CTkMessagebox(title="Erro", message="Informe o nome do paciente", icon="cancel", option_1="OK")
        return

    if not validar_data(data_nascimento):
        CTkMessagebox(title="Erro", message="Data inválida! Use DD/MM/AAAA", icon="cancel", option_1="OK")
        return

    if not validar_telefone(telefone):
        CTkMessagebox(title="Erro", message="Telefone inválido", icon="cancel", option_1="OK")
        return

    # lê pacientes
    with open(caminho, "r", encoding="utf-8") as f:
        pacientes = json.load(f)

    # atualiza paciente
    for p in pacientes:
        if p["id"] == paciente_id:
            p["nome"] = nome
            p["data_nascimento"] = data_nascimento
            p["email"] = email
            p["telefone"] = telefone
            p["cpf/rg"] = cpf_rg
            p["genero"] = genero
            break

    # salva
    with open(caminho, "w", encoding="utf-8") as f:
        json.dump(pacientes, f, indent=4)

    # atualiza Treeview
    from utils.funçoes import carregar_pacientes
    carregar_pacientes(treeview)

    CTkMessagebox(title="Sucesso", message="Paciente atualizado!", icon="check", option_1="OK")



def editar_sobre_detalhe(paciente, detalhe_frame, treeview,app):
    # Cria frame de edição sobre o detalhe_frame
    editar_frame = ctk.CTkFrame(detalhe_frame, fg_color="white")
    editar_frame.place(relx=0.5, rely=0.5, anchor="center")  # centraliza sobre o detalhe_frame
    editar_frame.configure(width=400, height=400)  # tamanho fixo

    entry_dict = {}

    # ===== NOME =====
    frame_nome = ctk.CTkFrame(editar_frame, fg_color="transparent")
    frame_nome.pack(fill="x", padx=20, pady=5)

    ctk.CTkLabel(frame_nome, text="Nome", text_color=AZUL_FONTE_TEXTO).pack(anchor="w")

    entry_nome = ctk.CTkEntry(frame_nome)
    entry_nome.pack(fill="x")
    entry_nome.insert(0, paciente[1])

    entry_dict["nome"] = entry_nome


    # ===== LINHA: DATA + CPF =====
    frame_linha = ctk.CTkFrame(editar_frame, fg_color="transparent")
    frame_linha.pack(fill="x", padx=20, pady=5)

    # DATA
    frame_data = ctk.CTkFrame(frame_linha, fg_color="transparent")
    frame_data.pack(side="left", expand=True, fill="x", padx=5)

    ctk.CTkLabel(frame_data, text="Data de Nascimento", text_color=AZUL_FONTE_TEXTO).pack(anchor="w")

    entry_data = ctk.CTkEntry(frame_data)
    entry_data.pack(fill="x")
    entry_data.insert(0, paciente[2])

    entry_dict["data_de_nascimento"] = entry_data


    # CPF
    frame_cpf = ctk.CTkFrame(frame_linha, fg_color="transparent")
    frame_cpf.pack(side="left", expand=True, fill="x", padx=5)

    ctk.CTkLabel(frame_cpf, text="CPF/RG", text_color=AZUL_FONTE_TEXTO).pack(anchor="w")

    entry_cpf = ctk.CTkEntry(frame_cpf)
    entry_cpf.pack(fill="x")
    entry_cpf.insert(0, paciente[5])

    entry_dict["cpf/rg"] = entry_cpf


    # ===== CONTATO =====
    frame_contato = ctk.CTkFrame(editar_frame, fg_color="transparent")
    frame_contato.pack(fill="x", padx=20, pady=5)

    # TELEFONE
    frame_tel = ctk.CTkFrame(frame_contato, fg_color="transparent")
    frame_tel.pack(side="left", expand=True, fill="x", padx=5)

    ctk.CTkLabel(frame_tel, text="Telefone", text_color=AZUL_FONTE_TEXTO).pack(anchor="w")

    entry_tel = ctk.CTkEntry(frame_tel)
    entry_tel.pack(fill="x")
    entry_tel.insert(0, paciente[4])

    entry_dict["telefone"] = entry_tel


    # EMAIL
    frame_email = ctk.CTkFrame(frame_contato, fg_color="transparent")
    frame_email.pack(side="left", expand=True, fill="x", padx=5)

    ctk.CTkLabel(frame_email, text="Email", text_color=AZUL_FONTE_TEXTO).pack(anchor="w")

    entry_email = ctk.CTkEntry(frame_email)
    entry_email.pack(fill="x")
    entry_email.insert(0, paciente[3])

    entry_dict["email"] = entry_email


    # ===== GENERO =====
    frame_genero = ctk.CTkFrame(editar_frame, fg_color="transparent")
    frame_genero.pack(fill="x", padx=20, pady=5)

    ctk.CTkLabel(frame_genero, text="Gênero", text_color=AZUL_FONTE_TEXTO).pack(anchor="w")

    combo = ctk.CTkComboBox(frame_genero, values=["Masculino", "Feminino", "Outro"])
    combo.pack(fill="x")
    combo.set(paciente[6])

    entry_dict["genero"] = combo


    # Botão salvar
    ctk.CTkButton(
        editar_frame,
        text="Salvar Alterações",
        command=lambda: salvar_edicao_sobre(paciente[0], entry_dict, treeview, editar_frame, app)
    ).pack(pady=10)



def salvar_edicao_sobre(paciente_id, entry_dict, treeview, editar_frame,app):
    caminho = CAMINHO_PACIENTES

    nome = entry_dict["nome"].get()
    data_nascimento = entry_dict["data_de_nascimento"].get()
    telefone = entry_dict["telefone"].get()
    email = entry_dict["email"].get()
    cpf_rg = entry_dict["cpf/rg"].get()
    genero = entry_dict["genero"].get()

    from utils.funçoes import validar_data, validar_telefone, carregar_pacientes, renderizar_detalhe

    # validações
    if not nome:
        CTkMessagebox(title="Erro", message="Informe o nome do paciente", icon="cancel", option_1="OK")
        return

    if not validar_data(data_nascimento):
        CTkMessagebox(title="Erro", message="Data inválida! Use DD/MM/AAAA", icon="cancel", option_1="OK")
        return

    if not validar_telefone(telefone):
        CTkMessagebox(title="Erro", message="Telefone inválido", icon="cancel", option_1="OK")
        return

    # 1. ler JSON
    with open(caminho, "r", encoding="utf-8") as f:
        pacientes = json.load(f)

    # 2. atualizar paciente
    for p in pacientes:
        if p["id"] == paciente_id:
            p["nome"] = nome
            p["data_nascimento"] = data_nascimento
            p["email"] = email
            p["telefone"] = telefone
            p["cpf/rg"] = cpf_rg
            p["genero"] = genero
            break

    # 3. salvar JSON
    with open(caminho, "w", encoding="utf-8") as f:
        json.dump(pacientes, f, indent=4)

    # 4. dados atualizados
    paciente_atualizado = [
        paciente_id,
        nome,
        data_nascimento,
        email,
        telefone,
        cpf_rg,
        genero
    ]

    # 5. atualizar detalhe (CORRETO)
    treeview_frame = editar_frame.master
    renderizar_detalhe(paciente_atualizado, treeview_frame, treeview,app)

    # 6. atualizar tabela
    if treeview and treeview.winfo_exists():
        carregar_pacientes(treeview)

    # 7. sucesso + fechar
    CTkMessagebox(title="Sucesso", message=f"Paciente {nome} atualizado!", icon="check", option_1="OK")

    editar_frame.after(100, editar_frame.destroy)




def renderizar_detalhe(paciente, treeview_frame, treeview, app):
    # limpa o frame
    for widget in treeview_frame.winfo_children():
        widget.destroy()

    detalhe_frame = ctk.CTkFrame(treeview_frame, fg_color="white")
    detalhe_frame.pack(fill="both", expand=True, padx=20, pady=20)

    labels = ["ID", "Nome", "Data de Nascimento", "Email", "Telefone","CPF/RG", "Genero"]

    for i, valor in enumerate(paciente):
        ctk.CTkLabel(
            detalhe_frame,
            text=f"{labels[i]}: {valor}",
            text_color="black"
        ).pack(pady=5, anchor="center")

    # botões
    ctk.CTkButton(
        detalhe_frame,
        text="Editar",
        command=lambda: editar_sobre_detalhe(paciente, detalhe_frame, treeview,app)
    ).pack(pady=5)

    ctk.CTkButton(
        detalhe_frame,
        text="Excluir",
        command=lambda: excluir_paciente(paciente, app)
    ).pack(pady=5)

    ctk.CTkButton(
        detalhe_frame,
        text="Registrar Atendimento",
        command=lambda: registrar_atendimento(paciente)
    ).pack(pady=5)


def trocar_tela(app, TelaClasse):
    for widget in app.frame_form.winfo_children():
        widget.destroy()

    tela = TelaClasse(app.frame_form, app)
    tela.pack(fill="both", expand=True, padx=20, pady=20)



# função de pesquisar no treeview
def pesquisar_pacientes(treeview, termo):
    import json
    import os

    caminho = CAMINHO_PACIENTES

    if not os.path.exists(caminho):
        return

    if termo == "":
        carregar_pacientes(treeview)
        return

    with open(caminho, "r", encoding="utf-8") as arquivo:
        pacientes = json.load(arquivo)

    # limpa a tabela
    for item in treeview.get_children():
        treeview.delete(item)

    termo = termo.lower()

    # filtra pacientes
    for paciente in pacientes:
        nome = paciente.get("nome", "").lower()
        telefone = paciente.get("telefone", "")

        if termo in nome or termo in telefone:
            treeview.insert("", "end", values=(
                paciente.get("id"),
                paciente.get("nome"),
                paciente.get("data_nascimento"),
                paciente.get("email"),
                paciente.get("telefone"),
                paciente.get("cpf/rg"),
                paciente.get("genero")
            ))
