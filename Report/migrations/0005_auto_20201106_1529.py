# Generated by Django 3.0.2 on 2020-11-06 15:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Report', '0004_auto_20201106_1430'),
    ]

    operations = [
        migrations.AddField(
            model_name='decision',
            name='activity',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='activity_decision', to='Report.Activity'),
        ),
        migrations.AddField(
            model_name='person',
            name='activity',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='activity_person', to='Report.Activity'),
        ),
        migrations.AddField(
            model_name='problem',
            name='activity',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='activity_problem', to='Report.Activity'),
        ),
    ]
