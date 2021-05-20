from django.shortcuts import render
# Create your views here.
from .models import List


def index(request):
    lists = List.objects.all()
    
    context={
        'page_title':'Guest List',
        'lists':lists,
        
    }
    return render(request,'list/index.html',context)



