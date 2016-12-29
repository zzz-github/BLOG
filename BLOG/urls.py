from django.conf.urls import patterns, include, url
from django.contrib import admin
from article import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'BLOG.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^index/(\d*)', views.index),
    url(r'^article/(\d+)/$', views.article),
    #url(r'^search/(\w+)/$', views.search),
    url(r'^search/$', views.search),
    url(r'^summernote/', include('django_summernote.urls')),
)
