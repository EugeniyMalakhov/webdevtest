# -*- coding: utf-8 -*-
from django.forms import ModelForm
from myapp.models import Comments, Articles, CommentToComment

#==================== Форма Сообщений (Message form) ===================================
class ArticleForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'text']

    def save(self, commit=True):
        article = super(ArticleForm, self).save(commit=False)
        if commit:
            article.save()
        return article

#==================== Форма комментария (Comment form) =================================
class CommentForm(ModelForm):
    class Meta:
        model = Comments
        fields = ['comment']

#================= Форма ответа на комментарий (Answer form) ===========================
class SubCommentsForm(ModelForm):
    class Meta:
        model = CommentToComment
        fields = ['subcomment']

#================= Форма редактирования сообщений (Не успел доделать)====================
class ChangeArticleForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'text']

    def save(self, commit=True):
        article = super(ChangeArticleForm, self).save(commit=False)
        article.title = self.cleaned_data['title']
        article.text = self.cleaned_data['text']

        if commit:
            article.save()

        return article