import wikipedia
from django.shortcuts import render
from datetime import datetime as dt

wikipedia.set_lang('ru')

def index(request):
	return render(
		request, 'index.html'
	)


def search(request):
    query = request.GET.get("q")
    
    try:
        page = wikipedia.page(query)
        return render(
            request, 'search.html',
            {
                'title': page.original_title,
                'summary': page.summary,
                'time': dt.now(),

                'parse': True
            }
        )
    except Exception as e:
        return render(
            request, 'search.html',
            {
                'error': '[ОШИБКА] Пожалуйста, введите корректное название!',
                'e': e,

                'parse': False
            }
        )