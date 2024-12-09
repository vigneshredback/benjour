# Generated by Django 5.1.4 on 2024-12-07 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_journal_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paper',
            name='issue',
        ),
        migrations.RenameField(
            model_name='paper',
            old_name='file',
            new_name='pdf_file',
        ),
        migrations.RenameField(
            model_name='paper',
            old_name='template_file',
            new_name='word_file',
        ),
        migrations.AddField(
            model_name='journal',
            name='journal_template_file',
            field=models.FileField(default=1, upload_to='uploads/template'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='journal',
            name='stylesheet_file',
            field=models.FileField(default=1, upload_to='uploads/stylesheet'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Issue',
        ),
    ]
