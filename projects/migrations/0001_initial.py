# Generated by Django 3.2.13 on 2022-07-05 14:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=10)),
                ('last_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='项目名称', max_length=200, unique=True, verbose_name='项目名称')),
                ('leader', models.CharField(help_text='负责人', max_length=50, verbose_name='负责人')),
                ('tester', models.CharField(help_text='测试人员', max_length=50, verbose_name='测试人员')),
                ('programer', models.CharField(help_text='开发人员', max_length=50, verbose_name='开发人员')),
                ('publist_app', models.CharField(help_text='应用名称', max_length=100, verbose_name='应用名称')),
                ('desc', models.TextField(blank=True, default='TEST', help_text='简要描述', null=True, verbose_name='简要描述')),
            ],
            options={
                'verbose_name': '项目',
                'verbose_name_plural': '项目',
                'db_table': 'tbl_projects',
            },
        ),
        migrations.CreateModel(
            name='Interface',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interface_name', models.CharField(help_text='项目名称', max_length=200, unique=True, verbose_name='接口名称')),
                ('leader', models.CharField(help_text='负责人', max_length=50, verbose_name='负责人')),
                ('tester', models.CharField(help_text='测试人员', max_length=50, verbose_name='测试人员')),
                ('project', models.ForeignKey(help_text='所属项目', on_delete=django.db.models.deletion.CASCADE, to='projects.projects', verbose_name='所属项目')),
            ],
            options={
                'verbose_name': '项目',
                'verbose_name_plural': '项目',
                'db_table': 'tbl_interface',
            },
        ),
    ]
