from . import views
from django.urls import path

app_name = 'craigsApp'

urlpatterns = [
    path('',views.home,name="home"),
]

#path('/new_search/', name="new_search") 