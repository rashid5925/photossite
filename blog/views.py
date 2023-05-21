from django.template import loader
from django.http import HttpResponse
from .models import Blog

def blog(request):
    template = loader.get_template("blog.html")
    post = Blog.objects.all()
    context = {
        'posts': post,
    }
    return HttpResponse(template.render(context, request))
