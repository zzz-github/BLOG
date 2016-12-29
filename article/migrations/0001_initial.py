# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50)),
                ('content', models.TextField()),
                ('keyword', models.CharField(max_length=20)),
                ('readed_count', models.IntegerField()),
                ('comment_count', models.IntegerField()),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Article_type',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('article_type', models.CharField(max_length=15)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comment_content', models.TextField(max_length=100)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('comment_article', models.ForeignKey(to='article.Article')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('reply_content', models.TextField(max_length=100)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=20)),
                ('icon', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='reply',
            name='create_by_user',
            field=models.ForeignKey(to='article.Users'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='reply',
            name='reply_comment',
            field=models.ForeignKey(to='article.Comment'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comment',
            name='created_by_user',
            field=models.ForeignKey(to='article.Users'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='article',
            name='article_type',
            field=models.ForeignKey(to='article.Article_type'),
            preserve_default=True,
        ),
    ]
