from django.shortcuts import render
from main.models import *

# Create your views here.
def index(request):
    context={}
    context['product'] = Product.objects.all()
    return render(request,'index.html',context)
