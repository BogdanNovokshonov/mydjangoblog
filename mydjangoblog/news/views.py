from django.shortcuts import render, redirect #redirect нужен чтоб перенаправить на другую страницу
from .models import Articles #наследуем модель
from .forms import ArticlesForm #наследуемся из forms.py
from django.views.generic import DetailView, UpdateView, DeleteView #На основе этого класса можно создать динамически изменяющуюся страницу


def news_home(request):
    news = Articles.objects.all()
    return render(request, 'news/news_home.html', {'news': news})

class NewsDetailView(DetailView):
    model = Articles
    template_name = 'news/details_view.html'
    context_object_name = 'article'

class NewsUpdateView(UpdateView):
    model = Articles
    template_name = 'news/create.html'

    form_class = ArticlesForm

class NewsDeleteView(DeleteView):
    model = Articles
    success_url = '/news/'
    template_name = 'news/news-delete.html'

def create(request):
    error = ''
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid(): #in class ModelForm forms.py
            form.save()
            return redirect('/news/')
        else:
            error = 'Вы неправильно ввели форму'
    form = ArticlesForm()

    data = {
        'form': form
    }
    return render(request, 'news/create.html', data)