# Generated by Django 2.2.6 on 2020-01-07 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0023_infotext'),
    ]

    operations = [
        migrations.AlterField(
            model_name='infotext',
            name='key',
            field=models.CharField(max_length=32, primary_key=True, serialize=False),
        ),
        migrations.AlterUniqueTogether(
            name='infotext',
            unique_together={('key',)},
        ),
        migrations.RemoveField(
            model_name='infotext',
            name='id',
        ),
    ]
