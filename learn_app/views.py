# Create your views here.
from django.http import HttpResponse
from django.template import Context, loader
from learn_app.models import Article,User,Comment

def index(request):
    article_list = Article.objects.all()[:5]

    t = loader.get_template('learn/index.html')
    c = Context({
        'article_list': article_list,
        })

    return HttpResponse(t.render(c))
