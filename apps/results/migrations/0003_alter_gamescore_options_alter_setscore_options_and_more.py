# Generated by Django 4.2.4 on 2023-09-13 13:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0002_fixture_fixtureresults_gamescore_setscore_tiebreaker_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='gamescore',
            options={'verbose_name_plural': 'Game Scores'},
        ),
        migrations.AlterModelOptions(
            name='setscore',
            options={'verbose_name_plural': 'Set Scores'},
        ),
        migrations.AlterModelOptions(
            name='tiebreaker',
            options={'verbose_name_plural': 'Tie Breaks'},
        ),
    ]
