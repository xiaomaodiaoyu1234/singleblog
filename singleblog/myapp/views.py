from django.shortcuts import render
from .models import Post
from django.http import HttpResponse
# from django.http import HttpResponse

# Create your views here.
def index(request,id):
    p_list = Post.objects.get(pk = id)
    cont={"pl":p_list}
    return render(request,'index.html',context=cont)
def detail(request):
    p_all = Post.objects.all()
    cone = {"pi":p_all}
    return render(request,'de.html',context=cone)

def date1(request,ad):
    return HttpResponse(f'{ad}一万年')