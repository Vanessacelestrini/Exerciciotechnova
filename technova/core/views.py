from django.shortcuts import render

servicosLista = [
        {
            'nome': 'Consultoria',
            'descricao': 'Consultoria especializada para melhorar sua estratégia de negócios.',
            'preco': 500.00
        },
        {
            'nome': 'Desenvolvimento Web',
            'descricao': 'Criação de sites personalizados e soluções web.',
            'preco': 1500.00
        },
        {
            'nome': 'Marketing Digital',
            'descricao': 'Serviços de marketing para aumentar sua visibilidade online.',
            'preco': 1000.00
        },
        {
            'nome': 'Design Gráfico',
            'descricao': 'Desenvolvimento de identidades visuais e material gráfico.',
            'preco': 800.00
        }
    ]

cursosLista = [
        {
            'nome': 'Desenvolvimento Web',
            'descricao': 'Curso completo de desenvolvimento web com HTML, CSS, JavaScript e Python.',
            'carga_horaria': 120,  # em horas
            'preco': 1200.00
        },
        {
            'nome': 'Marketing Digital',
            'descricao': 'Curso de estratégias de marketing digital, SEO, anúncios e mídias sociais.',
            'carga_horaria': 80,
            'preco': 800.00
        },
        {
            'nome': 'Design Gráfico',
            'descricao': 'Aprenda a criar identidades visuais e design de interfaces com ferramentas como Photoshop e Illustrator.',
            'carga_horaria': 100,
            'preco': 900.00
        },
        {
            'nome': 'Data Science',
            'descricao': 'Introdução ao mundo da ciência de dados, incluindo análise de dados, estatísticas e Machine Learning.',
            'carga_horaria': 150,
            'preco': 1500.00
        }
    ]


def home(request):
    return render(request, 'home.html')

def sobre(request):
    return render(request, 'sobre.html')

def contato(request):
    return render(request, 'contato.html')

def cursos(request):
    return render(request, 'cursos.html', {'cursos': cursosLista})

def servicos(request):
    return render(request, 'servicos.html', {'servicos': servicosLista})

def navbar(request):
    return render(request, 'navbar.html')