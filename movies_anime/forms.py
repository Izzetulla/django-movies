from django import forms
from .models import Title, Genre


class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = ["name"]
        labels = {"name": "Название жанра"}


class TitleForm(forms.ModelForm):
    status = forms.ChoiceField(
        label="Статус",
        choices=[
            ("Хочу посмотреть", "Хочу посмотреть"),
            ("Смотрю", "Смотрю"),
            ("Посмотрел", "Посмотрел"),
        ],
    )
    rating = forms.IntegerField(
        label="Оценка (1-10)",
        min_value=1,
        max_value=10,
        required=False,
        error_messages={
            "min_value": "Оценка не может быть меньше 1.",
            "max_value": "Оценка не может быть больше 10.",
            "invalid": "Введите целое число.",
        },
    )

    class Meta:
        model = Title
        fields = ["name", "genre", "status", "rating"]
        labels = {"name": "Название", "genre": "Жанр"}