# Generated by Django 4.0.4 on 2022-06-15 15:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('screamer_api', '0003_alter_actor_death_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='release_year',
            new_name='release_date',
        ),
        migrations.RenameField(
            model_name='productioncompany',
            old_name='years_active',
            new_name='year_founded',
        ),
        migrations.AlterField(
            model_name='movie',
            name='director',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='directed_by', to='screamer_api.director'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='genre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='screamer_api.genre'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]