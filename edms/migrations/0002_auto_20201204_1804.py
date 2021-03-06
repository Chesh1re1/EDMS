# Generated by Django 3.1.3 on 2020-12-04 11:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('edms', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contr',
            old_name='contractor_name',
            new_name='contr_name',
        ),
        migrations.RenameField(
            model_name='contr',
            old_name='contractor_patronymic',
            new_name='contr_patronymic',
        ),
        migrations.RenameField(
            model_name='contr',
            old_name='contractor_surname',
            new_name='contr_surname',
        ),
        migrations.RenameField(
            model_name='doc',
            old_name='reg_date',
            new_name='doc_reg_date',
        ),
        migrations.RenameField(
            model_name='doc',
            old_name='uodate_date',
            new_name='doc_uodate_date',
        ),
        migrations.RenameField(
            model_name='doc',
            old_name='id_contractor',
            new_name='id_contr',
        ),
        migrations.RenameField(
            model_name='doc',
            old_name='registar_name',
            new_name='reg_name',
        ),
        migrations.RenameField(
            model_name='doc',
            old_name='registar_patronymic',
            new_name='reg_patronymic',
        ),
        migrations.RenameField(
            model_name='doc',
            old_name='registar_surname',
            new_name='reg_surname',
        ),
    ]
