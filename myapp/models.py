# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models

# python.exe C:\WebServers\webdev\manage.py runserver

#============================== Модель записей на стене ======================================
class Articles(models.Model):
    title = models.CharField(verbose_name='Заголовок', max_length=100)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User)

    class Meta():
        db_table = 'articles'
        ordering = ['-date']    # для вывода новых сообщений первыми

    def __unicode__(self):
        return self.title

#============================= Модель комментариев =============================================
class Comments(models.Model):
    class Meta():
        db_table = 'comments'

    def __unicode__(self):
        return self.comment

    comment = models.TextField(verbose_name="Добавить коментарий")
    date = models.DateTimeField(auto_now_add=True)
    article = models.ForeignKey(Articles)
    user = models.ForeignKey(User)

#============================== Модель для второго уровня комментариев =========================
class CommentToComment(models.Model):
    class Meta():
        db_table = 'subcomments'

    subcomment = models.TextField(verbose_name="Коментарий")
    date = models.DateTimeField(auto_now_add=True)
    comment = models.ForeignKey(Comments)
    user = models.ForeignKey(User)

