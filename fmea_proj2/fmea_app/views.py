from django.shortcuts import render
from django.http import HttpResponse
from fmea_app.models import Fmea_Record
from django.views.generic import ListView, CreateView # new
from django.urls import reverse_lazy # new
from .forms import PostForm # new
from .models import Fmea_Record


def index(request):
    webpage_list = Fmea_Record.objects.order_by("RPN")
    date_dict ={"access_records":webpage_list}
    return render(request,'fmea_app/index.html',context=date_dict)

class CreatePostView(CreateView): # new
    model = Fmea_Record
    form_class = PostForm
    template_name = 'post.html'
    success_url = reverse_lazy('index')
