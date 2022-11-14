from django.urls import path

from .views import IndexView, AboutView, ContectView
urlpatterns = [
    path('', IndexView.as_view()),
    path('about/', AboutView.as_view()),
    path('contect/', ContectView.as_view()),

]