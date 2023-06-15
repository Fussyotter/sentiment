from django.contrib import admin
from .models import Company, Comment

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)
    ordering = ('name',)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'company', 'text', 'sentiment_score')
    search_fields = ('company__name', 'text')
    ordering = ('company__name', 'sentiment_score')
