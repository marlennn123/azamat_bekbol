# Generated by Django 5.0.6 on 2024-07-02 16:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_faculty', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_professor', models.CharField(max_length=32)),
                ('title', models.CharField(max_length=32)),
                ('bio', models.TextField()),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='task.faculty')),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_course', models.CharField(max_length=32)),
                ('code', models.CharField(max_length=16)),
                ('description', models.TextField()),
                ('price', models.PositiveSmallIntegerField(default=0)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='task.faculty')),
                ('professor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='task.professor')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_student', models.CharField(max_length=32)),
                ('enrollment_date', models.DateField()),
                ('graduation_date', models.DateField(blank=True, null=True)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='task.faculty')),
            ],
        ),
    ]
