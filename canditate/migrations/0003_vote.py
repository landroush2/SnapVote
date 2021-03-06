# Generated by Django 3.1.3 on 2020-12-05 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elector', '0006_elector_candidate_id'),
        ('canditate', '0002_candidate_votes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vote_title', models.CharField(blank=True, max_length=255, null=True)),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField(blank=True, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_edites', models.DateTimeField(auto_now=True)),
                ('candidates', models.ManyToManyField(to='canditate.Candidate')),
                ('voters', models.ManyToManyField(to='elector.Elector')),
            ],
        ),
    ]
