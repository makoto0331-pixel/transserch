from django.urls import path
from .import views
from .views import searchView

app_name='transport'

urlpatterns = [
    path('',views.IndexView.as_view(),name='index'),
    path('test/',views.TestView.as_view(),name='test'),
    path('search/',searchView,name='search'),
]