from django.contrib import admin
from .models import Author, Practice, CodeLanguage


# admin.site.register(Author)
# Define the admin class


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'department', 'practices')


admin.site.register(Author, AuthorAdmin)


# admin.site.register(Practice)
@admin.register(Practice)
class PracticeAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date_of_latest_submit')
    list_filter = ('author', 'title')


# admin.site.register(CodeLanguage)
@admin.register(CodeLanguage)
class CodeLanguageAdmin(admin.ModelAdmin):
    pass
