# Generated by Django 3.1.6 on 2021-12-15 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_text', models.TextField(verbose_name='Текст поста')),
                ('date', models.DateTimeField(verbose_name='Дата публикации')),
            ],
            options={
                'verbose_name': 'Запись',
                'verbose_name_plural': 'Записи',
            },
        ),
    ]