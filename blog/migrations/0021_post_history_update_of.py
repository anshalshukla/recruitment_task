# Generated by Django 2.1.5 on 2020-01-08 13:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0020_post_history'),
    ]

    operations = [
        migrations.AddField(
            model_name='post_history',
            name='update_of',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.Post'),
        ),
    ]