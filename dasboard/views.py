from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from datetime import datetime, timedelta
import random

# @login_required
def dashboard_overview(request):
    """
    View principal do dashboard com métricas simuladas
    """
    # Simulando dados de métricas
    context = {
        'total_usuarios': random.randint(1200, 1500),
        'atividades_realizadas': random.randint(8500, 9200),
        'contas_criadas_hoje': random.randint(15, 45),
        'usuarios_ativos_mes': random.randint(800, 1000),
        'cursos_completados': random.randint(320, 450),
        'tempo_medio_sessao': f"{random.randint(12, 25)} min",
        'taxa_conclusao': f"{random.randint(68, 85)}%",
        'ultima_atualizacao': timezone.now().strftime("%d/%m/%Y às %H:%M"),
        
        # Dados para gráficos futuros
        'usuarios_ultimos_7_dias': [
            random.randint(20, 50) for _ in range(7)
        ],
        'dias_semana': ['Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sáb', 'Dom']
    }
    
    return render(request, 'overview.html', context)

def home_view(request):
    return render(request, 'dashboard.html')
