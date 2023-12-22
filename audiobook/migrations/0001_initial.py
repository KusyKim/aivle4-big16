# Generated by Django 5.0 on 2023-12-22 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('book_id', models.AutoField(primary_key=True, serialize=False)),
                ('book_title', models.CharField(max_length=255)),
                ('book_genre', models.CharField(default='Others', max_length=255)),
                ('book_image_path', models.ImageField(blank=True, upload_to='book_images/')),
                ('book_author', models.CharField(max_length=255)),
                ('book_publisher', models.CharField(max_length=255)),
                ('book_publication_date', models.DateField()),
                ('book_content_path', models.FileField(null=True, upload_to='book_contents/')),
                ('book_description', models.TextField()),
                ('book_likes', models.IntegerField(default=0)),
                ('book_isbn', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Voice',
            fields=[
                ('voice_id', models.AutoField(primary_key=True, serialize=False)),
                ('voice_name', models.CharField(max_length=255)),
                ('voice_like', models.IntegerField(default=0)),
                ('voice_path', models.TextField()),
                ('voice_image_path', models.TextField()),
                ('voice_created_date', models.DateTimeField(auto_now_add=True)),
                ('voice_is_public', models.BooleanField(default=False)),
            ],
        ),
    ]