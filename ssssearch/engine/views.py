from django.shortcuts import render
from engine.search import duck


def query(request):
    return render(request, 'engine/home.html')

def results(request):
    if request.method == "POST":
        query = request.POST.get('search')
        link, text = duck(query)
        data = zip(link, text)
        if query == "":
            return render(request, 'engine/home.html')
        else:
            return render(request, 'engine/results.html', {'results': data})



def about(request):
    return render(request, 'engine/about.html')