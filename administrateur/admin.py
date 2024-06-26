from django.contrib import admin
from .models import Question, Quizz, Association, Theme
from quizz.models import User

class AssociationAdmin(admin.ModelAdmin):
    list_display = ('idQuizz', 'idQuestion')

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('pseudo', 'id')

class ThemeAdmin(admin.ModelAdmin):
    list_display = ('pseudo', 'theme')


class QuizzAdmin(admin.ModelAdmin):
    list_display = ('pseudo', 'id')


admin.site.register(Question, QuestionAdmin)
admin.site.register(Quizz, QuizzAdmin)
admin.site.register(Association, AssociationAdmin)
admin.site.register(User)
admin.site.register(Theme, ThemeAdmin)

