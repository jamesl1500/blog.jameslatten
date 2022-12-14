# Generated by Django 4.1.1 on 2022-10-30 01:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_jobs_alter_post_cover'),
    ]

    operations = [
        migrations.CreateModel(
            name='Certs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cert_title', models.CharField(max_length=255)),
                ('cert_subjects', models.CharField(max_length=255)),
                ('cert_desc', models.TextField()),
                ('cert_link', models.CharField(max_length=255)),
                ('cert_image', models.ImageField(upload_to='static/storage/images/')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('cert_status', models.IntegerField(choices=[(0, 'Draft'), (1, 'In Progress'), (2, 'Obtained')], default=0)),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
        migrations.AlterField(
            model_name='jobs',
            name='job_date',
            field=models.CharField(max_length=200),
        ),
    ]
