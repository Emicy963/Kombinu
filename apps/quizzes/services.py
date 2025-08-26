import requests


import logging


logger = logging.getLogger(__name__)

# Mapeamento de categorias locais para categorias da Open Trivia DB
# Você pode obter os IDs reais chamando https://opentdb.com/api_category.php
CATEGORY_MAPPING = {
    "tecnologia": 18, # Science: Computers
    "negocios": 9999, # # Não há categoria direta, pode usar "Any Category" (sem ID) ou outra
    "design": 9999, # Nao há categoria direta
}

def get_opentdb_categories():
    """Obtém a lista de categorias da Open Trivia DB."""
    try:
        response = requests.get("https://opentdb.com/api_category.php")
        response.raise_for_status()
        data = response.json()
        return {cat["name"]: cat["id"] for cat in data.get("trivia_categories", [])}
    except requests.RequestException as e:
        logger.error("Erro ao buscar categorias da Open Trivia DB: {e}")
        return {}

def map_local_category_to_opentdb(local_category):
    """Mapeia a categoria local para o ID da Open Trivia DB."""
    # Atualiza o mapeamento com os IDs reais
    opentdb_categories = get_opentdb_categories()
    # Exemplo de mapeamento mais dinâmico
    mapping = {
        "tecnologia": opentdb_categories.get("Science: Computers", ""),
        "negocios": "", # Qualquer categoria ou específica
        "design": "", # Qualquer categoria ou específica
    }
    return mapping.get(local_category, "") # Retorna vazio para "Any Category"
