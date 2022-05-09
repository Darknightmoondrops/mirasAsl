# Generated by Django 4.0.4 on 2022-05-07 08:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Derakhti', '0004_alter_mainuser_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lusers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Derakhti.mainuser', verbose_name='Main')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
    ]