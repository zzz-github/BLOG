#!/usr/bin/env python
#-*-coding:utf-8-*-
__author__ = 'zhangzz'

from django.utils.safestring import mark_safe

class PageInfo():
    def __init__(self,page_num,article_count,per_page_news_num=5):
        self.Page_num = page_num
        self.News_count = article_count
        self.Per_page_news_num = per_page_news_num

    @property
    def start(self):
        return (self.Page_num-1) * self.Per_page_news_num

    @property
    def end(self):
        return self.Page_num * self.Per_page_news_num

    @property
    def page_count(self):
        temp = divmod(self.News_count,self.Per_page_news_num)
        if temp[1] == '0':
            page_count = temp[0]
        else:
            page_count = temp[0]+1
        return page_count

def Pager(page_num, page_count):
    page_html = []   #定义一个存放分页a标签的空列表

    first_html = '<li class="disabled"><a href="/index/%d">first</a></li>'%(1,)  #定义首页a标签
    page_html.append(first_html)  #往存放分页a标签的空列表追加首页a标签

    if page_num <= 1:
        prev_html = '<li class="disabled"><a href="#">&laquo;</a></li>'
    else:
        prev_html = '<li class=""><a href="/index/%d">&laquo;</a></li>'%(page_num-1,)
    page_html.append(prev_html)

    if page_count < 9:
        begin = 0
        end = page_count
    else:
        if page_num < 5:
            begin = 0
            end = 9
        else:
            if page_num+5 >= page_count:
                begin = page_num -5
                end = page_count
            else:
                begin = page_num - 5
                end = page_num + 4

    html_1 = '<li class="active"><a href="/index/%d">1<span class="sr-only">(current)</span></a></li>'%(1,)
    page_html.append(html_1)
    for i in range(begin+1,end):
        a_html = '<li class="" onclik="changePage(this);"><a href="/index/%d">%d</a></li>'%(i+1,i+1)  #循环生成分页a标签，并追加到page_html
        page_html.append(a_html)

    if page_num >= page_count:
        next_html = '<li class=""><a href="#">&raquo;</a></li>'
    else:
        next_html = '<li class=""><a href="/index/%d">&raquo;</a></li>'%(page_num+1,)
    page_html.append(next_html)

    last_html = '<li><a href="/index/%d">last</a></li>'%(page_count,)  #生成尾页
    page_html.append(last_html)  #插入尾页
    page_string = mark_safe(' '.join(page_html))  #把所有分页a标签拼接，并通过django的mark_safe返回html给前端

    return page_string