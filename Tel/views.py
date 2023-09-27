
from django.shortcuts import render
from django.utils import timezone
from .models import Tel

from Tel.forms import SearchForm

def base_search(form):
    
    return Tel.objects.filter(FIO__icontains = form['FIO'],
                               number__icontains = form['number'],
                               text__icontains = form['text'])
def search(request):
    print("До if")
    if request.method == 'GET':
        form = SearchForm(request.GET)
        print("После if")
        if form.is_valid():
            print("Форма проверена")
            results = base_search(form.cleaned_data)
           ## results = base_search(form.cleaned_data)
            form = SearchForm()
            if not results.exists(): results = "none"
            return render(request,'post_list.html', {'form': form, 'results': results})
    else:
        form = SearchForm()
    return render(request, 'post_list.html', {'form': form})


def post_list(request):
    tels = Tel.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

    return render(request, 'post_list.html', {'posts': tels})
# Create your views here.
