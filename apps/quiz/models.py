from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from django.db import models


class QuizCategory(models.Model):
    name = models.CharField(max_length=255, verbose_name=_("Soha nomi"))
    image = models.ImageField(upload_to="sohalar/", verbose_name=_("Soha rasmi"))
    description = models.TextField(verbose_name=_("Soha haqida"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Yaratilgan sana"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Yangilangan sana"))
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Soha")
        verbose_name_plural = _("Sohalar")



class Quiz(models.Model):
    title = models.CharField(max_length=255, verbose_name=_("Savol sarlavhasi"))
    description = models.TextField(verbose_name=_("Savol haqida"))
    soha = models.ForeignKey(QuizCategory, on_delete=models.CASCADE, verbose_name=_("Soha"))
    quiz_time = models.IntegerField(verbose_name=_("Test vaqti"), default=0)
    is_active = models.BooleanField(default=False, verbose_name=_("Faol"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Yaratilgan sana"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Yangilangan sana"))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Test")
        verbose_name_plural = _("Testlar")

    def get_answers_count(self,):
        count = QuizQuestion.objects.filter(quiz=self).count()
        return count


class QuizQuestion(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, verbose_name=_("Savol"))
    question = models.TextField(verbose_name=_("Savol haqida"))
    is_active = models.BooleanField(default=False, verbose_name=_("Faol"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Yaratilgan sana"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Yangilangan sana"))

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = _("Savol")
        verbose_name_plural = _("Savollar")

    def get_answers_count(self,):
        count = Answer.objects.filter(quiz=self).count()
        return count
    

    def get_all_answers(self):
        return Answer.objects.filter(quiz=self)
    
class Answer(models.Model):
    quiz = models.ForeignKey(QuizQuestion, on_delete=models.CASCADE, verbose_name=_("Savol"))
    text = models.CharField(max_length=255, verbose_name=_("Javob"))
    is_correct = models.BooleanField(default=False, verbose_name=_("To'g'ri javob"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Yaratilgan sana"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Yangilangan sana"))

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = _("Javob")
        verbose_name_plural = _("Javoblar")

    
class QuizTaker(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_("Foydalanuvchi"))
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, verbose_name=_("Savol"))
    correct_answers = models.IntegerField(default=0, verbose_name=_("To'g'ri javoblar soni"))
    mistakes = models.IntegerField(default=0, verbose_name=_("Xato javoblar soni"))
    completed = models.BooleanField(default=False, verbose_name=_("Yechildi"))
    start_timestamp = models.DateTimeField(auto_now_add=True, verbose_name=_("Boshlangan sana"))
    timestamp = models.DateTimeField(auto_now=True, verbose_name=_("Yechilgan sana"))

    def __str__(self):
        return self.user.username + ' - ' + self.quiz.title

    class Meta:
        verbose_name = _("Test oluvchi")
        verbose_name_plural = _("Test oluvchilar")


    def get_answers(self):
        return self.quiz.get_answers_count