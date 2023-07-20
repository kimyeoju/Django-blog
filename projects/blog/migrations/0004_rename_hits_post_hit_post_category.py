# Generated by Django 4.2.3 on 2023-07-19 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_hits'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='hits',
            new_name='hit',
        ),
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('자유', '자유'), ('취미', '취미'), ('리뷰', '리뷰')], default='자유', max_length=30),
        ),
    ]