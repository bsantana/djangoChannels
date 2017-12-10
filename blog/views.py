from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from .models import Post

# Create your views here.

# def post_list(request):
#     return HttpResponse("Hello, worasasdadld. You're at the polls in2dex. NEW")
def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'blog/post_list.html', {'posts': posts})