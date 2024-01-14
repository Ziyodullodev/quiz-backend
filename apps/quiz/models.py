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
    quiz_time = models.IntegerField(verbose_name=_("Test vaqti"))
    is_active = models.BooleanField(default=False, verbose_name=_("Faol"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Yaratilgan sana"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Yangilangan sana"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Savol")
        verbose_name_plural = _("Savollar")

    
class Answer(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, verbose_name=_("Savol"))
    text = models.CharField(max_length=255, verbose_name=_("Javob"))
    is_correct = models.BooleanField(default=False, verbose_name=_("To'g'ri javob"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Yaratilgan sana"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Yangilangan sana"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Javob")
        verbose_name_plural = _("Javoblar")

    
class QuizTaker(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_("Foydalanuvchi"))
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, verbose_name=_("Savol"))
    correct_answers = models.IntegerField(default=0, verbose_name=_("To'g'ri javoblar soni"))
    completed = models.BooleanField(default=False, verbose_name=_("Yechildi"))
    start_timestamp = models.DateTimeField(auto_now_add=True, verbose_name=_("Boshlangan sana"))
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name=_("Yechilgan sana"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Test oluvchi")
        verbose_name_plural = _("Test oluvchilar")