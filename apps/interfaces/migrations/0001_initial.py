# Generated by Django 3.2.14 on 2022-10-19 08:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Interface',
            fields=[
                ('create_time', models.DateTimeField(auto_now_add=True, help_text='创建时间', verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now_add=True, help_text='更新时间', verbose_name='更新时间')),
                ('is_delete', models.BooleanField(default=False, help_text='逻辑删除', verbose_name='逻辑删除')),
                ('id', models.AutoField(help_text='id主键', primary_key=True, serialize=False, verbose_name='id主键')),
                ('interface_name', models.CharField(help_text='项目名称', max_length=200, unique=True, verbose_name='接口名称')),
                ('leader', models.CharField(help_text='负责人', max_length=50, verbose_name='负责人')),
                ('tester', models.CharField(help_text='测试人员', max_length=50, verbose_name='测试人员')),
                ('desc', models.TextField(blank=True, default='接口简要描述', help_text='简要描述', null=True, verbose_name='简要描述')),
                ('project', models.ForeignKey(help_text='所属项目', on_delete=django.db.models.deletion.CASCADE, to='projects.projects', verbose_name='所属项目')),
            ],
            options={
                'verbose_name': '接口测试',
                'verbose_name_plural': '接口测试',
                'db_table': 'tbl_interface',
            },
        ),
    ]
