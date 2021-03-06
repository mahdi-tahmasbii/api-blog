# Generated by Django 4.0 on 2021-12-16 09:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('blog', '0003_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Comment', models.ManyToManyField(blank=True, related_name='like', to='blog.Comment')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='like', to='auth.user')),
                ('posts', models.ManyToManyField(blank=True, related_name='like', to='blog.Post')),
            ],
            options={
                'verbose_name_plural': 'likes',
            },
        ),
    ]
