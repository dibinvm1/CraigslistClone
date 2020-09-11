import requests

from .models import Search
from bs4 import BeautifulSoup
from django.shortcuts import render
from requests.compat import quote_plus

BASE_URL = 'https://bangalore.craigslist.org/search/?query={}'
BASE_IMG_URL = 'https://images.craigslist.org/{}_300x300.jpg'

def home(request):
    return render(request,'craigsApp/base.html')

def new_search(request):
    if request.POST:
        search = request.POST.get('search')
        Search.objects.create(search=search)
        url = BASE_URL.format(quote_plus(search))
    
        response = requests.get(url)
        soup = BeautifulSoup(response.text, features='html.parser')
        posts = soup.find_all('li', {'class' : 'result-row'})
        post_list = []
        for post in posts:
            post_title = post.find(class_='result-title').text
            post_url = post.find('a').get('href')
            if post.find(class_ = 'result-price'):
                post_price = post.find(class_ = 'result-price').text
            else :
                post_price = "N/A"
            if post.find(class_='result-image').get('data-ids'):
                post_iamge = BASE_IMG_URL.format(post.find(class_='result-image').get('data-ids').split(',')[0][2:])
            else:
                post_iamge = 'https://craigslist.org/images/peace.jpg'
            post_list.append((post_title,post_url,post_price,post_iamge))

        context = {
            'search' : search,
            'post_list' : post_list
        }
        return render(request,'craigsApp/search.html', context)
    return render(request,'craigsApp/search.html')
