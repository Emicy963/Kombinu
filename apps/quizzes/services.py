import requests
import html
from django.db import transaction
from .models import Option, Question, Quiz


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

def generate_quiz_from_opentdb(content, difficulty=None, num_questions=10):
    """
    Gera um quiz chamando a API da Open Trivia DB.
    """
    category_id = map_local_category_to_opentdb(content.category)
    logger.debug(f"Mapaemento de categoria: {content.category} -> {category_id}")

    params = {
        "amount": num_questions,
        "type": "multiple", # Assume múltipla escolha
        "encode": "url3986" # Para lidar com caracteres especias
    }
    if category_id:
        params["category"] = category_id
    if difficulty:
        params["difficulty"] = difficulty

    api_url = "https://opentdb.com/api.php"
    try:
        response = requests.get(api_url, params=params)
        response.raise_for_status()
        data = response.json()

        if data["response_code"] != 0:
            logger.error(f"Erro da API Open Trivia DB: {data["response_code"]}")
            return None
        
        questions_data = data["results"]

        with transaction.atomic():
            # Cria o quiz
            quiz_title = f"Quiz: {content.title}"
            quiz = Quiz.objects.create(title=quiz_title, content=content)

            for q_data in questions_data:
                # Decodifica entendida HTML
                question_text = html.unescape(q_data["question"])
                correct_answer = html.unescape(q_data["correct_answer"])
                incorrect_answers = [html.unescape(ans) for ans in q_data["incorrect_answers"]]

                # Cria a questão
                question_obj = Question.objects.create(
                    quiz=quiz,
                    question_text=question_text
                )

                # Cria a opção correta
                Option.objects.create(
                    question=question_obj,
                    text=correct_answer,
                    is_correct=True
                )

                # Cria as opções incorretas
                for inc_ans in incorrect_answers:
                    Option.objects.create(
                        question=question_obj,
                        text=inc_ans,
                        is_correct=False
                    )
            
            return quiz
    except requests.RequestException as e:
        logger.error(f"Erro ao chamar a API da Open Trivia DB: {e}")
        return None
    except Exception as e:
        logger.error(f"Erro inesperado ao gerar o quiz: {e}")
        return None
