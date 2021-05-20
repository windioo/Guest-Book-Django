from django.shortcuts import render
from django.http import HttpResponseRedirect
from list.forms import PostForm
from list.models import List


def index(request):
    post_form = PostForm()
    if request.method == 'POST':
        List.objects.create(
            nama = request.POST['nama'],
            email = request.POST['email'],
            alamat = request.POST['alamat'],
        )
        return HttpResponseRedirect("/list/")
    context = {
       'page_title':'FORM GUEST BOOK',
       'post_form':post_form,
       
     }
    return render(request, 'index.html',context)