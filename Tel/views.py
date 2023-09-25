from django.shortcuts import render
from .forms import SearchForm

def post_search(request): 
    form = SearchForm() 
    query = None 
    results = [] 
    if 'query' in request.GET: 
        form = SearchForm(request.GET) 
        if form.is_valid(): 
            query = form.cleaned_data['query'] 
            results = Post.objects.annotate(
                search=SearchVector('title', 'body'), 
            ).filter(search=query) 
    return render(request, 
                  'blog/post/search.html', 
                  {'form': form, 
                   'query': query, 
                   'results': results})
# Create your views here.
