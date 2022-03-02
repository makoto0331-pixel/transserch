from django.shortcuts import render
from django.views.generic import TemplateView
from .Transfers import transfers
class IndexView(TemplateView):
    print("sss")
    template_name = 'home.html'

class TestView(TemplateView):
    print("aaa")
    template_name = 'search.html'

def searchView(request):
    depurture = request.POST['depurture']
    destination = request.POST['destination']
    accept = transfers(depurture,destination)
    return render(request,'search.html',{'somedata':100,'accept':accept})
    