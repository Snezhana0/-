# Generated by Django 3.2.16 on 2022-12-20 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='faq',
            options={'ordering': ['id', 'title'], 'verbose_name': 'Статьи вкладки "FAQ"', 'verbose_name_plural': 'Статьи вкладки "FAQ"'},
        ),
        migrations.AlterField(
            model_name='faq',
            name='content',
            field=models.TextField(blank=True, verbose_name='Ответ'),
        ),
        migrations.AlterField(
            model_name='faq',
            name='is_published',
            field=models.BooleanField(default=True, verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='faq',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Вопрос'),
        ),
    ]