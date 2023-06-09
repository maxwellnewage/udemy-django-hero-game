# Generated by Django 4.1.7 on 2023-03-29 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('character', '0002_player_armor_player_hands_player_head_player_legs'),
    ]

    operations = [
        migrations.CreateModel(
            name='Enemy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('hp', models.IntegerField(default=5)),
                ('money_drop', models.IntegerField(default=0)),
                ('attack', models.IntegerField()),
                ('defense', models.IntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
