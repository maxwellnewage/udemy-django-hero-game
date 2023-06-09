# Generated by Django 4.1.7 on 2023-03-28 14:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
        ('character', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='armor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='armor', to='shop.weapon'),
        ),
        migrations.AddField(
            model_name='player',
            name='hands',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='hands', to='shop.weapon'),
        ),
        migrations.AddField(
            model_name='player',
            name='head',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='head', to='shop.weapon'),
        ),
        migrations.AddField(
            model_name='player',
            name='legs',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='legs', to='shop.weapon'),
        ),
    ]
