from django.shortcuts import render, redirect
from .models import Articles, Comments
from .forms import ArticlesForm, CommentsForm
from django.views.generic import DetailView, UpdateView, DeleteView


def news_home(request):
    news = Articles.objects.order_by('-date')
    return render(request, 'news/news_home.html', {'news': news})

class NewsDetailView(DetailView):
    model = Articles
    template_name = 'news/details_view.html'
    context_object_name = 'article'

class NewsUpdateView(UpdateView):
    model = Articles
    template_name = 'news/create.html'

    form_class = ArticlesForm   # fields = ['full_text', 'date']

class NewsDeleteView(DeleteView):
    model = Articles
    success_url = '/news/'
    template_name = 'news/news-delete.html'





class PostCommentView(DetailView):
    model = Articles
    template_name = 'news/comment/comment.html'
    context_object_name = 'article'

    comments = Comments.objects.order_by('-date')
    extra_context = {'comments': comments}

    


    





def create(request):
    error = ''
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news_home')
        else:
            error = 'Форма была неверной'
    
    form = ArticlesForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'news/create.html', data)




def create_comment(request):
    error = ''
    if request.method == 'POST':
        form = CommentsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news_home')
        else:
            error = 'Форма была неверной'
    
    form = CommentsForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'news/comment/create-comment.html', data)