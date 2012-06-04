# Create your views here.
from django.http import HttpResponse
from django.template import Context, loader
from learn_app.models import Article,User,Comment

def index(request):
    latest_article_list = Article.objects.all()[:5]

    t = loader.get_template('learn_app/index.html')
    c = Context({
        'latest_article_list': latest_article_list,
        })

    return HttpResponse(t.render(c))
