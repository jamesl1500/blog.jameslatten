# Generated by Django 4.1.1 on 2022-10-17 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_cover'),
    ]

    operations = [
        migrations.CreateModel(
            name='Jobs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(max_length=255)),
                ('job_location', models.CharField(max_length=255)),
                ('job_desc', models.TextField()),
                ('job_date', models.TextField()),
                ('job_added', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-job_added'],
            },
        ),
        migrations.AlterField(
            model_name='post',
            name='cover',
            field=models.ImageField(upload_to='static/storage/images/'),
        ),
    ]
