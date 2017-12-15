# Generated by Django 2.0 on 2017-12-14 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Developers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('surname', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('university', models.CharField(max_length=50)),
                ('year_of_graduation', models.DateField()),
                ('developers', models.ManyToManyField(related_name='university', to='developers.Developers')),
            ],
        ),
        migrations.CreateModel(
            name='Empl_history',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=50)),
                ('role', models.CharField(max_length=30)),
                ('fr', models.DateField(verbose_name='from')),
                ('to', models.DateField()),
                ('developers', models.ManyToManyField(related_name='company', to='developers.Developers')),
            ],
        ),
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skills', models.CharField(max_length=100)),
                ('developers', models.ManyToManyField(related_name='skills', to='developers.Developers')),
            ],
        ),
    ]