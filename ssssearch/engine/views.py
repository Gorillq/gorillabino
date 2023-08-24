from django.shortcuts import render

from bs4 import BeautifulSoup
import requests


def query(request):
    return render(request, 'engine/home.html')

def results(request):
    if request.method == "POST":
        query = request.POST.get('search')
        if query == "":
            return render(request, 'engine/home.html')
        else:

            results = []
            #type api key
            page = requests.get('https://www.googleapis.com/customsearch/v1?key=your_api_key&cx=c380acb00f58141eb&q='+query).text
            soup = BeautifulSoup(page)
            listings = soup.find_all(class_="items")
            for content in listings:
                title = content.find(class_='title').text
                description = content.find(class_='snippet').text
                link = content.find(class_='link').text
                url = content.find(class_='formattedUrl').text
                results.append((title,description,url))
            context = {
                'results':results
            }
            return render(request, 'engine/results.html', context)
    else:
        return render(request, 'engine/results.html')


def about(request):
    return render(request, 'engine/about.html')