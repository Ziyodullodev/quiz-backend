from .models import QuizCategory, Quiz, QuizQuestion, Answer, QuizTaker
from django.contrib import admin


class QuizCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at', 'updated_at')
    list_display_links = ('id', 'name')
    list_filter = ('name',)
    search_fields = ('name', 'description')
    list_per_page = 25


class QuizAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'soha', 'created_at', 'updated_at')
    list_display_links = ('id', 'title')
    list_filter = ('title','soha',)
    search_fields = ('title', 'description')
    list_per_page = 25


class QuizquestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'quiz', 'question',)
    list_display_links = ('id', 'quiz')
    list_filter = ('quiz',)
    search_fields = ('quiz', 'question',)
    list_per_page = 25


class AnswerAdmin(admin.ModelAdmin):
    list_display = ('id', 'quiz', 'is_correct', 'created_at', 'updated_at')
    list_display_links = ('id',)
    list_filter = ('quiz', 'is_correct', 'created_at',)
    search_fields = ('quiz', 'is_correct')
    list_per_page = 25


class QuizTakerAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'quiz', 'correct_answers', 'mistakes', 'completed', 'start_timestamp', 'timestamp')
    list_display_links = ('id', 'user')
    list_filter = ('user', 'quiz', 'correct_answers', 'completed', 'start_timestamp', 'timestamp')
    search_fields = ('user', 'quiz', 'correct_answers', 'completed', 'start_timestamp', 'timestamp')
    list_per_page = 25




admin.site.register(QuizCategory, QuizCategoryAdmin)
admin.site.register(QuizTaker, QuizTakerAdmin)
admin.site.register(QuizQuestion, QuizquestionAdmin)
admin.site.register(Answer, AnswerAdmin)
admin.site.register(Quiz, QuizAdmin)