from django.shortcuts import render, redirect, get_object_or_404
from .models import Title
from .forms import TitleForm


def index(request):
    titles = Title.objects.all()
    return render(request, "movies/index.html", {"titles": titles})


def create(request):
    if request.method == "POST":
        form = TitleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = TitleForm()
    return render(request, "movies/form.html", {"form": form, "heading": "Добавить"})


def edit(request, id):
    title = get_object_or_404(Title, id=id)
    if request.method == "POST":
        form = TitleForm(request.POST, instance=title)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = TitleForm(instance=title)
    return render(request, "movies/form.html", {"form": form, "heading": "Изменить"})


def delete(request, id):
    get_object_or_404(Title, id=id).delete()
    return redirect("/")