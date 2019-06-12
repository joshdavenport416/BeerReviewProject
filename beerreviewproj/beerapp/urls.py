from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('gettypes/', views.gettypes, name='types'),
    path('getbeers/', views.getbeers, name='beers'),
    path('beerdetails/<int:id>', views.beerdetails, name='beerdetails'),
    path('newBeer/', views.newBeer, name='newbeer'),
    path('newReview/', views.newReview, name='newreview'),
    path('loginmessage/', views.loginmessage, name='loginmessage'),
    path('logoutmessage/', views.logoutmessage, name='logoutmessage'),
]