from . import views
from django.urls import path

app_name = 'craigsApp'

urlpatterns = [
    path('', views.home, name="home"),
    path('search/', views.new_search , name="new_search")
]