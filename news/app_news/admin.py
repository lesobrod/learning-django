from django.contrib import admin
from .models import News, Comment, Profile


def truncate(text):
    if len(text) <= 15:
        return text
    return text[:15] + '...'


class CommentInline(admin.TabularInline):
    model = Comment


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline,
    ]
    list_display = ['title', 'created_at', 'status']
    fieldsets = (
        ('Новость', {
            'fields': ('title', 'description', 'status')
        }),
        ('Для администратора', {
            'fields': ('admin_comment', 'age_rate'),
            'description': 'Для администратора',
            'classes': ['collapse']
        }),
    )
    list_filter = ['status']
    actions = ['mark_draft', 'mark_archive', 'mark_published']

    def mark_draft(self, request, queryset):
        queryset.update(status='d')

    def mark_archive(self, request, queryset):
        queryset.update(status='a')

    def mark_published(self, request, queryset):
        queryset.update(status='p')

    mark_draft.short_description = 'Сделать статус Черновик'
    mark_archive.short_description = 'Сделать статус Архив'
    mark_published.short_description = 'Сделать статус Опубликовано'


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['author', 'short_text']
    list_filter = ['author']
    actions = ['mark_spam']

    def short_text(self, obj):
        return truncate(obj.text)

    def mark_spam(self, request, queryset):
        queryset.update(text='Удалено администратором')

    mark_spam.short_description = 'Пометить как спам'
    short_text.short_description = 'Текст'


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user',  'is_verified']