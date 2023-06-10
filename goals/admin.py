from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from goals.models import GoalCategory, GoalComment, Goal


@admin.register(GoalCategory)
class GoalCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    readonly_fields = ('created', 'updated')
    list_filter = ['is_deleted']
    search_fields = ['title']


class CommentsInline(admin.StackedInline):
    model = GoalComment
    extra = 0


@admin.register(Goal)
class GoalAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author_link')
    search_fields = ('title', 'description')
    readonly_fields = ('created', 'updated')
    list_filter = ('status', 'priority')
    inlines = [CommentsInline]

    # ссылка на автора для админки
    def author_link(self, obj: Goal) -> str:
        return format_html(
            "<a href='{url}'>(user_name)</a>",
            url=reverse('admin:core_user_change', kwargs={'object_id': obj.user_id}),
        )

    author_link.short_description = 'Author'


