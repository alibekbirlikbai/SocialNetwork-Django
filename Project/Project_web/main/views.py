from django.shortcuts import render
from news.models import Articles

def index(request):
    return render(request, 'news/news_home.html')

def about(request):
    return render(request, 'main/other-pages/about.html')
    


def friends(request):
    return render(request, 'main/other-pages/friends.html')

def messenger(request):
    return render(request, 'main/other-pages/messenger.html')

def profile(request):
    news = Articles.objects.order_by('-date')
    return render(request, 'main/other-pages/my-profile.html', {'news': news})

def support(request):
    return render(request, 'main/other-pages/support.html')




def feedback(request):
    return render(request, 'main/other-pages/feedback.html')