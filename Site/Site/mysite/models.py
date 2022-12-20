from django.db import models
from django.urls import reverse


class Faq(models.Model):
    title =models.CharField(max_length=255, verbose_name="Вопрос")
    content = models.TextField(blank=True, verbose_name="Ответ")
    is_published=models.BooleanField(default=True, verbose_name="Статус")

    def __str__(self):
        return self.title


    class Meta:
        verbose_name='Статьи вкладки "FAQ"'
        verbose_name_plural='Статьи вкладки "FAQ"'
        ordering =['id', 'title']