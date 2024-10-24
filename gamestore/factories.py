import factory
from factory.django import ImageField

from gamestore import models


class GameFactory(factory.django.DjangoModelFactory):
    title = factory.Faker('sentence')
    price = factory.Faker('pyfloat')
    description = factory.Faker('text')

    class Meta:
        model = models.Game

class StatisticsFactory(factory.django.DjangoModelFactory):
    review_score = factory.Faker('text')
    review_count = factory.Faker('text')
    times_bought = factory.Faker('text')
    game = factory.SubFactory(GameFactory)

    class Meta:
        model = models.Statistics