from .models import Articles, Comments
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea

class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['full_text', 'date']

        widgets = {
            "date":DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата публикации'

            }),
            "full_text":Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Текст'
            })

        }


class CommentsForm(ModelForm):
    class Meta:
        model = Comments
        fields = ['comment', 'date']

        widgets = {
            "date":DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата публикации'

            }),
            "comment":Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Комментарий'
            })

        }