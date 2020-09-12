# Generated by Django 3.1.1 on 2020-09-12 18:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ad',
            options={},
        ),
        migrations.RenameField(
            model_name='ad',
            old_name='date',
            new_name='created_at',
        ),
        migrations.RemoveField(
            model_name='ad',
            name='photos',
        ),
        migrations.AddField(
            model_name='ad',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='')),
                ('ad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='ads.ad')),
            ],
        ),
    ]
