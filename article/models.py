from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    article_type = models.ForeignKey('Article_type')
    keyword = models.CharField(max_length=20)
    readed_count = models.IntegerField()
    comment_count = models.IntegerField()
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now_add=True)
    def __unicode__(self):
        return self.title

class Article_type(models.Model):
    article_type = models.CharField(max_length=15)
    def __unicode__(self):
        return self.article_type

class Users(models.Model):
    username = models.CharField(max_length=20)
    icon = models.CharField(max_length=100)

class Comment(models.Model):
    comment_content = models.TextField(max_length=100)
    comment_article = models.ForeignKey('Article')
    create_date = models.DateTimeField(auto_now_add=True)
    created_by_user = models.ForeignKey('Users')
    def __unicode__(self):
        return self.comment_content

class Reply(models.Model):
    reply_content = models.TextField(max_length=100)
    reply_comment = models.ForeignKey('Comment')
    create_date = models.DateTimeField(auto_now_add=True)
    create_by_user = models.ForeignKey('Users')
    def __unicode__(self):
        return self.reply_content
