from django.contrib import admin
from myapp.models import Articles, Comments, CommentToComment


class ArticleInLine(admin.StackedInline):
    model = Comments
    extra = 1

class ArticleAdmin(admin.ModelAdmin):
    fields = ['title', 'text']
    inlines = [ArticleInLine]

admin.site.register(Articles, ArticleAdmin)

class SubCommentsInLine(admin.StackedInline):
    model = CommentToComment
    extra = 1

class CommentAdmin(admin.ModelAdmin):
    fields = ['comment']
    inlines = [SubCommentsInLine]

admin.site.register(Comments, CommentAdmin)