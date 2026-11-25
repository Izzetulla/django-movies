from django.shortcuts import render, redirect, get_object_or_404
from .models import Title, Genre
from .forms import TitleForm


def index(request):
    titles = Title.objects.order_by("-id")     

    name = request.GET.get("q")
    genre = request.GET.get("genre")
    status = request.GET.get("status")

    if genre:
        titles = titles.filter(genre_id=genre)  
    if status:
        titles = titles.filter(status=status)  
    if name:
        titles = [t for t in titles if name.lower() in t.name.lower()]

    return render(request, "movies/index.html", {
        "titles": titles,
        "genres": Genre.objects.all(),
        "statuses": ["Хочу посмотреть", "Смотрю", "Посмотрел"],
    })


def detail(request, id):
    title = get_object_or_404(Title, id=id)
    return render(request, "movies/detail.html", {"title": title})


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
            return redirect("detail", id=title.id)
    else:
        form = TitleForm(instance=title)
    return render(request, "movies/form.html", {"form": form, "heading": "Изменить"})


def delete(request, id):
    get_object_or_404(Title, id=id).delete()
    return redirect("/")