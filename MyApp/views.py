from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils import timezone
from django.db.models import F
from .models import Post, Comment
from .forms import PostForm, PostDeleteForm, CommentForm
from django.shortcuts import redirect
from MyApp2.models import norm

def post_list(request):
    queryset_list = Post.objects.all()
    paginator = Paginator(queryset_list, 3)

    page = request.GET.get('page', 1)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        # fallback to the first page
        queryset = paginator.page(1)
    except EmptyPage:
        # probably the user tried to add a page number
        # in the url, so we fallback to the last page
        queryset = paginator.page(paginator.num_pages)

    context = {
        "posts": queryset,

    }
    return render(request, 'blog/post_list.html', context)

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.views = post.views + 1
    post.save()
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):

    form = PostForm()
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            # post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    form = PostForm()
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            # post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})


def post_remove(request, pk=None):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostDeleteForm(request.POST, instance=post)
        if form.is_valid():
            post.delete()
            return redirect('/')
    else:
        form = PostDeleteForm(instance=post)
    return render(request, 'blog/delete.html', {'form': form,'post': post,})


def post_draft_list(request):
    posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'blog/post_draft_list.html', {'posts': posts})

def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_detail', pk=pk)

def publish(self):
    self.published_date = timezone.now()
    self.save()



def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment_to_post.html', {'form': form})



@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('post_detail', pk=comment.post.pk)

@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('post_detail', pk=comment.post.pk)


# def post_view(request, pk):
#     post = Post.objects.get(pk=pk)
#     post.views = F('views') + 1
#     post.save()
#     print(post.cleaned_data)
#
#     return render(request, 'post_detail.html', {'post': post})


