import hmac
import os

from dotenv import load_dotenv

from utils.caminhos import BASE_DIR


load_dotenv(BASE_DIR / ".env")


def credenciais_configuradas():
    return bool(os.getenv("CARESYNC_USUARIO") and os.getenv("CARESYNC_SENHA"))


def autenticar(usuario, senha):
    usuario_esperado = os.getenv("CARESYNC_USUARIO", "")
    senha_esperada = os.getenv("CARESYNC_SENHA", "")
    return hmac.compare_digest(usuario, usuario_esperado) and hmac.compare_digest(senha, senha_esperada)
