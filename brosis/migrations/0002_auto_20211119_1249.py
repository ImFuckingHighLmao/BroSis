# Generated by Django 3.2.9 on 2021-11-19 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brosis', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='id',
            field=models.BigAutoField(default=None, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='message',
            name='text',
            field=models.CharField(choices=[('Sis!', 'Sis!')], default=None, max_length=4),
        ),
    ]