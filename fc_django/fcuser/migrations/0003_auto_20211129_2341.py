# Generated by Django 3.2.9 on 2021-11-29 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fcuser', '0002_alter_fcuser_password'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fcuser',
            old_name='register',
            new_name='register_date',
        ),
        migrations.AddField(
            model_name='fcuser',
            name='level',
            field=models.CharField(choices=[('aemin', 'admin'), ('user', 'user')], default='user', max_length=8, verbose_name='등급'),
            preserve_default=False,
        ),
    ]
