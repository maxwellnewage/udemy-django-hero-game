# Generated by Django 4.1.7 on 2023-03-28 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Weapon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('money_cost', models.IntegerField()),
                ('attack', models.IntegerField(default=0)),
                ('defense', models.IntegerField(default=0)),
                ('type', models.CharField(choices=[('HEAD', 'Casco'), ('HAND', 'Una Mano'), ('LEGS', 'Piernas'), ('ARMOR', 'Armadura')], default=None, max_length=5)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
    ]
