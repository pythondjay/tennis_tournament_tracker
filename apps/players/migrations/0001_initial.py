# Generated by Django 4.2.4 on 2023-08-30 15:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tournaments', '0002_remove_tournaments_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('code', models.CharField(max_length=3, primary_key=True, serialize=False)),
                ('country_name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Countries',
            },
        ),
        migrations.CreateModel(
            name='Players',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('gender', models.CharField(max_length=1)),
                ('date_of_birth', models.DateField()),
                ('country_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='players.country')),
            ],
            options={
                'verbose_name_plural': 'Players',
            },
        ),
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registration_date', models.DateField()),
            ],
            options={
                'verbose_name_plural': 'Registration',
            },
        ),
        migrations.CreateModel(
            name='RegistrationPlayer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='players.players')),
                ('registration', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='players.registration')),
            ],
        ),
        migrations.CreateModel(
            name='PlayingIn',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seed', models.IntegerField()),
                ('registration_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='players.registration')),
                ('tournament_playing_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tournaments.tournamentplayingcategory')),
            ],
            options={
                'verbose_name_plural': 'Playing In',
            },
        ),
    ]
