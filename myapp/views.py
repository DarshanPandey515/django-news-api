from django.shortcuts import render,get_object_or_404
from myapp.models import PostModel
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.


def index(request):
    try:
        article_obj = PostModel.objects.all()
        paginator = Paginator(article_obj, 10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
    except Exception as e:
        print(e)
    context = {
        'article_obj':article_obj,
        'page_obj':page_obj,
    }
    return render(request,'index.html',context)


def detail(request,slug):
    post_obj = get_object_or_404(PostModel,slug=slug)
    context = {
        'post_obj':post_obj,
    }
    return render(request,'detail.html',context)