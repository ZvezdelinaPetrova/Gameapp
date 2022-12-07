from django.core.validators import MinLengthValidator, MinValueValidator, MaxLengthValidator


from django.core import validators, exceptions
from django.db import models


def validate_rating(value):
    if not 0.1 <= value <= 5.0:
        raise exceptions.ValidationError("Year must be between 0.1 and 5.0")


class Profile(models.Model):

    email = models.EmailField(
        null=False,
        blank=False,
    )

    age = models.IntegerField(
        validators=[MinValueValidator(12)],
        null=False,
        blank=False,
    )

    password = models.CharField(
        max_length=30,
        null=False,
        blank=False,
    )

    first_name = models.CharField(
        max_length=30,
        null=True,
        blank=True,
    )

    last_name = models.CharField(
        max_length=30,
        null=True,
        blank=True,

    )

    image = models.URLField(
        null=True,
        blank=True,
    )


class Game(models.Model):

    types_game = (
        ("Action", "Action"),
        ("Adventure", "Adventure"),
        ("Puzzle", "Puzzle"),
        ("Strategy", "Strategy"),
        ("Sports", "Sports"),
        ("Board/Card Game", "Board/Card Game"),
        ("Other", "Other"),
    )

    title = models.CharField(max_length=30, unique=True, null=False, blank=False, )

    category = models.CharField(
        max_length=15,
        choices=types_game,
        null=False,
        blank=False,
    )

    max_level = models.IntegerField(
        validators=[MinValueValidator(1)],
        null=True,
        blank=True,
    )

    image_url = models.URLField(
        null=False,
        blank=False,
    )

    rating = models.FloatField(
        null=False,
        blank=False,
        validators=(
            validate_rating,
        )
    )

    summary = models.TextField(
        null=True,
        blank=True,
    )

    class Meta:
        ordering = ('pk',)