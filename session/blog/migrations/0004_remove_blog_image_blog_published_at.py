# Generated by Django 5.0.3 on 2024-03-26 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_remove_blog_accesstoken_blog_image_alter_blog_mail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='image',
        ),
        migrations.AddField(
            model_name='blog',
            name='published_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
