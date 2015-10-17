from django.shortcuts import render
import datetime
from django.utils import timezone
from .models import Post


def post_list(request):
	right_now = datetime.datetime.now()
	
	Posts = Post.objects.exclude(published_date = None).filter(published_date__lte=timezone.now()).order_by("-published_date")
	return render(request, "index.html", {"time": right_now, "posts": Posts})

