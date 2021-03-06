# Generated by Django 2.2.6 on 2019-10-28 14:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attachment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='')),
                ('comment', models.TextField()),
                ('uploader', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='activitytype',
            name='files',
            field=models.ManyToManyField(to='app.Attachment'),
        ),
        migrations.AddField(
            model_name='event',
            name='files',
            field=models.ManyToManyField(to='app.Attachment'),
        ),
    ]
