import datetime
from django.contrib import admin
from django.utils import timezone

from .models import Question, Choice


# Register your models here.
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    list_filter = ['pub_date']

    list_display = ('question_text','pub_date','was_published_recently')
    inlines = [ChoiceInline]
    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)
