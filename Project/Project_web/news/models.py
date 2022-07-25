from django.db import models

class Articles(models.Model):
    full_text = models.TextField('Пост (Текст)')
    date = models.DateTimeField('Дата публикации')

    def __str__(self):
        return self.full_text

    def get_absolute_url(self):
        return f'/news/{self.id}'

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'



class Comments(models.Model):
    comment = models.TextField('Комментарий')
    date = models.DateTimeField('Дата публикации')

    def __str__(self):
        return self.comment

    def get_absolute_url(self):
        return f'/news/{self.id}'

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
    

