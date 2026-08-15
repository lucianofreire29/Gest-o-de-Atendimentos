# CareSync — Gestão de Atendimentos

Aplicação desktop para cadastro de pacientes, registro de atendimentos e visualização de indicadores. Desenvolvida como projeto de estudos em Python.

> Este é um projeto educacional. Não utilize dados reais de pacientes nem o trate como sistema clínico de produção.

## Funcionalidades

- autenticação por credenciais configuradas no ambiente;
- cadastro, consulta, edição e exclusão de pacientes;
- registro e histórico de atendimentos;
- pesquisa de pacientes;
- dashboard com indicadores e gráficos;
- persistência local em arquivos JSON.

## Tecnologias

- Python 3
- CustomTkinter e CTkMessagebox
- Pillow
- Tkcalendar
- Matplotlib
- Python Dotenv

## Estrutura

```text
.
├── assets/          # Imagens da interface
├── cards_frame/     # Telas e componentes
├── constantes/      # Cores e constantes visuais
├── data/            # Dados locais ignorados pelo Git
│   └── exemplos/    # Arquivos fictícios de referência
├── utils/           # Autenticação, caminhos e funções auxiliares
├── .env.example
├── main.py
└── requirements.txt
```

## Instalação

```bash
git clone https://github.com/lucianofreire29/Gest-o-de-Atendimentos.git
cd Gest-o-de-Atendimentos
python -m venv .venv
```

Ative o ambiente virtual e instale as dependências:

```bash
pip install -r requirements.txt
```

## Configuração

Copie `.env.example` para `.env` e defina credenciais próprias:

```env
CARESYNC_USUARIO=seu_usuario
CARESYNC_SENHA=uma_senha_forte
```

O arquivo `.env` é ignorado pelo Git e não deve ser publicado.

## Execução

```bash
python main.py
```

Os arquivos `data/pacientes.json` e `data/atendimentos.json` serão criados localmente conforme a aplicação for utilizada. O diretório `data/exemplos` contém apenas registros fictícios.

## Segurança e privacidade

- não publique credenciais no repositório;
- não versione os JSONs gerados pela aplicação;
- use somente dados fictícios durante demonstrações;
- para uso real, substitua arquivos JSON por banco de dados, controle de acesso, auditoria e criptografia adequados.

## Autor

**Luciano Freire**

- GitHub: [@lucianofreire29](https://github.com/lucianofreire29)
