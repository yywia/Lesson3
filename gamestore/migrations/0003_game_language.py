# Generated by Django 5.1.1 on 2024-10-08 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gamestore', '0002_game_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='language',
            field=models.CharField(choices=[('RU', 'Русский'), ('EN', 'Английский'), ('FR', 'Французский'), ('ES', 'Испанский'), ('DE', 'Немецкий'), ('IT', 'Итальянский'), ('NL', 'Нидерландский'), ('PL', 'Польский'), ('PT', 'Португальский'), ('TR', 'Турецкий')], default='ru', max_length=255, verbose_name='Язык'),
        ),
    ]
