from django.shortcuts import render
from blog.models import Post, Comment
from blog.forms import CommentForm

# Create your views here.

def blog_index(request):
  posts = Post.objects.all().order_by('-created_on') # order most recent post first
  context = {
    "posts":posts,
  }
  return render(request, "blog_index.html", context)


def blog_category(request,category):
  posts = Post.objects.filter(
      categories_name_contains=category).order_by("-created_on")

  context = {
    "category": category,
    "posts": posts
  }
  return render(request, "blog_category.html", context)

def blog_detail(request,pk):
  post = Post.objects.get(pk=pk)

  # insert the comment form here
  form = CommentForm()
  if request.method == 'POST':
    form = CommentForm(request.POST)
    if form.is_valid(): #checking if fields are entered correctly
      comment = Comment(
          author=form.cleaned_data["author"],
          body = form.cleaned_data["body"],
          post = post
      )
      comment.save()

  comments = Comment.objects.filter(post=post)
  context = {
    "post":post,
    "comments":comments,
    "form":form # addded the form to add more comments to the render
  }
  return render (request, "blog_detial.html", context)

