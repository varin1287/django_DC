from django.shortcuts import render
from django.views.generic.base import View
from .models import Post


class HomeView(View):
    def get(self, request):
        context = {'posts': Post.objects.all()}
        return render(request, 'blog/home.html', context)
