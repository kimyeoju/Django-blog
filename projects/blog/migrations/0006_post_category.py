# Generated by Django 4.2.3 on 2023-07-20 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_remove_post_category_hashtag_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('Daily', 'Daily'), ('Review', 'Review')], default='Daily', max_length=30),
        ),
    ]