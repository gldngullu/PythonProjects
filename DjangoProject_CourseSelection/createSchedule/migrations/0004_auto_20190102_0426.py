# Generated by Django 2.0.9 on 2019-01-02 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('createSchedule', '0003_course_coursehourend'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='courseHourEnd',
            field=models.IntegerField(choices=[(0, '9.00'), (1, '10.00'), (2, '11.00'), (3, '12.00'), (4, '13.00'), (5, '14.00'), (6, '15.00'), (7, '16.00'), (8, '17.00')], default=None),
        ),
        migrations.AlterField(
            model_name='course',
            name='courseHourStart',
            field=models.IntegerField(choices=[(0, '9.00'), (1, '10.00'), (2, '11.00'), (3, '12.00'), (4, '13.00'), (5, '14.00'), (6, '15.00'), (7, '16.00'), (8, '17.00')], default=None),
        ),
    ]
