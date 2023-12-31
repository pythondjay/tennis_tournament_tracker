# Generated by Django 4.2.4 on 2023-08-30 16:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tournaments', '0002_remove_tournaments_name'),
        ('results', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fixture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_player', models.CharField(max_length=255)),
                ('second_player', models.CharField(max_length=255)),
                ('round', models.IntegerField()),
                ('tournament_playing_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tournaments.tournamentplayingcategory')),
            ],
        ),
        migrations.CreateModel(
            name='FixtureResults',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('winners_name', models.CharField(max_length=255)),
                ('runner_up_name', models.CharField(max_length=255)),
                ('is_opponent_retired', models.CharField(max_length=1)),
                ('fixture_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='results.fixture')),
            ],
            options={
                'verbose_name_plural': 'Results',
            },
        ),
        migrations.CreateModel(
            name='GameScore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('set_number', models.IntegerField()),
                ('game_number', models.IntegerField()),
                ('first_registration_point', models.IntegerField()),
                ('second_registration_point', models.IntegerField()),
                ('fixture_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='results.fixture')),
            ],
        ),
        migrations.CreateModel(
            name='SetScore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('set_number', models.IntegerField()),
                ('first_registration_games', models.IntegerField()),
                ('second_registration_games', models.IntegerField()),
                ('fixture_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='results.fixture')),
            ],
        ),
        migrations.CreateModel(
            name='TieBreaker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('set_number', models.IntegerField()),
                ('first_registration_breaker', models.IntegerField()),
                ('second_registration_breaker', models.IntegerField()),
                ('fixture_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='results.fixture')),
            ],
        ),
        migrations.DeleteModel(
            name='Results',
        ),
    ]
