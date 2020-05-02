from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import norm
from .forms import addnewform


def form_list(request):
    losts = norm.objects.filter()
    return render(request, 'clog/form_list.html', {'losts': losts} )

def form_detail(request, pk):
    lost = get_object_or_404(norm, pk=pk)
    return render(request, 'clog/form_detail.html', {'lost': lost})

def add_form(request):
    if request.method == "POST":
        form1 = addnewform(request.POST)

        if form1.is_valid():
            post = form1.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()

    else:
        form1 = addnewform()
    return render(request, 'clog/form_edit.html', {'form1' :form1})


def form_edit(request):
    post = get_object_or_404(norm, pk=pk)
    if request.method == "POST":
        form1 = addnewform(request.POST, instance=post)

        if form1.is_valid():
            post = form1.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()

    else:
        form1 = addnewform(instance=post)
    return render(request, 'clog/form_edit', {'form1' :form1})