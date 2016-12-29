#!/usr/bin/env python
#coding:utf-8
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from article import models
# Register your models here.


# Apply summernote to all TextField in model.
class SomeModelAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    pass

#注册其他类的时候可以使用SomeModelAdmin
admin.site.register(models.Article,SomeModelAdmin)