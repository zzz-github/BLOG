from django.shortcuts import render
from django.shortcuts import render_to_response
from django.shortcuts import HttpResponse
from django.template.context import RequestContext
from django.db.models import Q
import models
import common
import html_helper
import pickle

# Create your views here.

def index(request,page):
    ret = {}
    all_article_count = models.Article.objects.all().count()
    page_num = common.try_int(page,1)
    article_pager_class = html_helper.PageInfo(page_num,all_article_count,)
    all_article_obj = models.Article.objects.all()[article_pager_class.start:article_pager_class.end]
    page_html_string = html_helper.Pager(page_num,article_pager_class.page_count)

    python_article_count = models.Article.objects.filter(article_type=1).count()
    python_article_pager_class = html_helper.PageInfo(page_num,python_article_count,)
    python_article_obj = models.Article.objects.filter(article_type=1)[python_article_pager_class.start:python_article_pager_class.end]
    page2_html_string = html_helper.Pager(page_num,python_article_pager_class.page_count)

    linux_article_count = models.Article.objects.filter(article_type=2).count()
    linux_article_pager_class = html_helper.PageInfo(page_num,linux_article_count,)
    linux_article_obj = models.Article.objects.filter(article_type=2)[linux_article_pager_class.start:linux_article_pager_class.end]
    page3_html_string = html_helper.Pager(page_num,linux_article_pager_class.page_count)

    sql_article_count = models.Article.objects.filter(article_type=3).count()
    sql_article_pager_class = html_helper.PageInfo(page_num,sql_article_count,)
    sql_article_obj = models.Article.objects.filter(article_type=3)[sql_article_pager_class.start:sql_article_pager_class.end]
    page4_html_string = html_helper.Pager(page_num,sql_article_pager_class.page_count)

    recommend = models.Article.objects.all().order_by('-readed_count')[:10]
    lately = models.Article.objects.all().order_by('-update_date')[:10]

    ret['article'] = all_article_obj
    ret['python'] = python_article_obj
    ret['linux'] = linux_article_obj
    ret['sql'] = sql_article_obj
    ret['page_html'] = page_html_string
    ret['page2_html'] = page2_html_string
    ret['page3_html'] = page3_html_string
    ret['page4_html'] = page4_html_string
    ret['recommend'] = recommend
    ret['lately'] = lately
    return render_to_response('index.html',ret,context_instance=RequestContext(request))

def article(request,article_id):
    ret = {}
    article_obj = models.Article.objects.get(id=article_id)
    article_obj.readed_count = article_obj.readed_count + 1
    article_obj.save()
    ret['article'] = article_obj
    return render_to_response('article.html',ret)

'''def search(request,keyword):
    ret = {}
    article_obj = models.Article.objects.filter(Q(content__icontains=keyword)|Q(title__icontains=keyword)|Q(article_type__article_type__icontains=keyword))
    ret['article'] = article_obj
    return render_to_response('index.html',ret)'''

def search(request):
    ret={}
    keyword = request.POST.get('keyword')
    article_obj = models.Article.objects.filter(Q(content__icontains=keyword)|Q(title__icontains=keyword)|Q(article_type__article_type__icontains=keyword))
    ret['article'] = article_obj
    return render_to_response('index.html',ret,context_instance=RequestContext(request))

