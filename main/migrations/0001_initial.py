# Generated by Django 3.2.16 on 2023-02-24 12:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Day',
            fields=[
                ('DayID', models.BigAutoField(primary_key=True, serialize=False)),
                ('Date', models.DateField()),
                ('AverageT', models.IntegerField()),
                ('AverageAH', models.IntegerField()),
                ('AverageSH', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Time',
            fields=[
                ('TimeID', models.BigAutoField(primary_key=True, serialize=False)),
                ('Time', models.TextField()),
                ('DayID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.day')),
            ],
        ),
        migrations.CreateModel(
            name='TemperatureValue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('S1', models.IntegerField()),
                ('S2', models.IntegerField()),
                ('S3', models.IntegerField()),
                ('S4', models.IntegerField()),
                ('AverageT', models.IntegerField()),
                ('DayID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.day')),
                ('TimeID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.time')),
            ],
        ),
        migrations.CreateModel(
            name='SoilHudimityValue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('S1', models.IntegerField()),
                ('S2', models.IntegerField()),
                ('S3', models.IntegerField()),
                ('S4', models.IntegerField()),
                ('AverageT', models.IntegerField()),
                ('DayID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.day')),
                ('TimeID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.time')),
            ],
        ),
        migrations.CreateModel(
            name='AirHudimityValue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('S1', models.IntegerField()),
                ('S2', models.IntegerField()),
                ('S3', models.IntegerField()),
                ('S4', models.IntegerField()),
                ('AverageT', models.IntegerField()),
                ('DayID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.day')),
                ('TimeID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.time')),
            ],
        ),
    ]
