# Generated by Django 2.2.10 on 2024-06-11 19:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('skills', models.CharField(blank=True, max_length=300, null=True)),
                ('experience', models.CharField(blank=True, max_length=300, null=True)),
                ('education', models.CharField(blank=True, max_length=300, null=True)),
                ('user_link', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, parent_link=True, related_name='custom_user', to='cv.Person')),
            ],
        ),
    ]
