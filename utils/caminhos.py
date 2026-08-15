from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
ASSETS_DIR = BASE_DIR / "assets"
DATA_DIR = BASE_DIR / "data"

CAMINHO_PACIENTES = DATA_DIR / "pacientes.json"
CAMINHO_ATENDIMENTOS = DATA_DIR / "atendimentos.json"
