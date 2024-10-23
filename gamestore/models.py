from django.db import models
from django.utils.translation.trans_null import get_language


# Create your models here.
class Game(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(verbose_name="Название", max_length=255, unique=True)
    description = models.TextField(verbose_name="Описание", blank=True)
    price = models.FloatField(verbose_name="Цена")
    release_date = models.DateField(verbose_name="Дата выхода", auto_now_add=True)
    update_time = models.DateField(verbose_name="Дата последнего обновления", auto_now=True)
    version = models.TextField(verbose_name="Версия", max_length=20, default="1.0.0")
    image = models.ImageField(verbose_name="Изображение", upload_to="games/", blank=True)
    is_available = models.BooleanField(verbose_name="Наличие", default=True)
    LANGUAGE_CHOICES = [
        ("RU", "Русский"),
        ("EN", "Английский"),
        ("FR", "Французский"),
        ("ES", "Испанский"),
        ("DE", "Немецкий"),
        ("IT", "Итальянский"),
        ("NL", "Нидерландский"),
        ("PL", "Польский"),
        ("PT", "Португальский"),
        ("TR", "Турецкий")
    ]
    language = models.CharField(verbose_name="Язык", max_length=255, default="ru", choices=LANGUAGE_CHOICES)
    publisher = models.ForeignKey(
        'Publisher',
        verbose_name="Издатель",
        related_name='games',
        on_delete=models.SET_NULL,
        null=True
    )



    class Meta:
        verbose_name = "Игра"
        verbose_name_plural = "Игры"
        ordering = ['title']

    def __str__(self):
        return self.title

    def get_discount_fall(self):
        return (self.price - (self.price * 0.25))


class Developer(models.Model):
    name = models.CharField(verbose_name="Разработчик", max_length=255, unique=True)
    description = models.TextField(verbose_name="Описание", blank=True)

    class Meta:
        verbose_name = "Разработчик"
        verbose_name_plural = "Разработчики"
        ordering = ['name']

    def __str__(self):
        return self.name

class Genre(models.Model):
    name = models.CharField('Жанр', max_length=255, unique=True)
    description = models.TextField('Описание', blank=True)
    game = models.ManyToManyField(
        Game,
        verbose_name="Игры",
        related_name='genres',
        blank=True,
    )

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"
        ordering = ['name']

    def __str__(self):
        return self.name

class Publisher(models.Model):
    name = models.CharField('Издатель', max_length=255, unique=True)
    description = models.TextField('Описание', blank=True)
    developer = models.ForeignKey(
        'Developer',
        verbose_name="Разработчик",
        related_name='games',
        on_delete=models.SET_NULL,
        null=True
    )

    class Meta:
        verbose_name = "Издатель"
        verbose_name_plural = "Издатели"
        ordering = ['name']

    def __str__(self):
        return self.name

class Statistics(models.Model):
    review_score = models.FloatField('Оценка', default=0.0)
    review_count = models.IntegerField('Количество отзывов', default=0)
    times_bought = models.IntegerField('Количество покупок', default=0)
    game = models.OneToOneField(
        Game,
        on_delete=models.CASCADE,
        related_name='statistics',
        blank=True,
        null=True,
        verbose_name="Игра"
    )

    class Meta:
        verbose_name = "Статистика"
        verbose_name_plural = "Статистики"
        ordering = ['review_score', 'review_count']

    def __str__(self):
        return f'{self.game} - {self.review_score}'

